class Book:
    """图书类"""
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.current_borrower = None  # 当前借阅者ID

    def __str__(self):
        # 基础状态显示，不带借阅者ID（用于SEARCH等命令）
        status = "Borrowed" if self.is_borrowed else "Available"
        return f'{self.isbn} "{self.title}" by {self.author} - {status}'


class BorrowRecord:
    """借阅记录类"""
    def __init__(self, record_id, book_isbn, borrower_id, borrow_date):
        self.record_id = record_id
        self.book_isbn = book_isbn
        self.borrower_id = borrower_id
        self.borrow_date = borrow_date
        self.return_date = None  # 初始未归还

    def mark_returned(self, return_date):
        """标记为已归还"""
        self.return_date = return_date


class Library:
    """图书馆管理类"""
    def __init__(self):
        self.books = {}  # ISBN -> Book对象
        self.borrow_records = {}  # record_id -> BorrowRecord对象
        self.next_record_id = 1
        self.borrower_records = {}  # borrower_id -> [record_ids]

    def add_book(self, isbn, title, author):
        """添加图书"""
        if isbn in self.books:
            return False, f"Error: Book {isbn} already exists"
        self.books[isbn] = Book(isbn, title, author)
        return True, f"Book {isbn} added"

    def remove_book(self, isbn):
        """移除图书"""
        if isbn not in self.books:
            return False, f"Error: Book {isbn} not found"
        book = self.books[isbn]
        if book.is_borrowed:
            return False, f"Error: Book {isbn} is borrowed"
        del self.books[isbn]
        return True, f"Book {isbn} removed"

    def borrow_book(self, isbn, borrower_id, borrow_date):
        """借阅图书"""
        if isbn not in self.books:
            return False, f"Error: Book {isbn} not found"
        book = self.books[isbn]
        if book.is_borrowed:
            return False, f"Error: Book {isbn} is already borrowed"
        # 创建借阅记录
        record_id = self.next_record_id
        self.next_record_id += 1
        record = BorrowRecord(record_id, isbn, borrower_id, borrow_date)
        self.borrow_records[record_id] = record
        # 更新借阅者记录
        if borrower_id not in self.borrower_records:
            self.borrower_records[borrower_id] = []
        self.borrower_records[borrower_id].append(record_id)
        # 更新图书状态
        book.is_borrowed = True
        book.current_borrower = borrower_id
        return True, f"Book {isbn} borrowed by {borrower_id}"

    def return_book(self, isbn, borrower_id, return_date):
        """归还图书"""
        if isbn not in self.books:
            return False, f"Error: Book {isbn} not found"
        book = self.books[isbn]
        if not book.is_borrowed or book.current_borrower != borrower_id:
            return False, f"Error: Book {isbn} is not borrowed by {borrower_id}"
        # 查找对应未归还的借阅记录
        target_record = None
        for record_id in self.borrower_records.get(borrower_id, []):
            record = self.borrow_records[record_id]
            if record.book_isbn == isbn and record.return_date is None:
                target_record = record
                break
        if not target_record:
            return False, f"Error: Book {isbn} is not borrowed by {borrower_id}"
        # 标记记录为已归还
        target_record.mark_returned(return_date)
        # 更新图书状态
        book.is_borrowed = False
        book.current_borrower = None
        return True, f"Book {isbn} returned by {borrower_id}"

    def search_books(self, keyword):
        """搜索图书（匹配ISBN、书名或作者）"""
        results = []
        for book in self.books.values():
            if keyword in book.isbn or keyword in book.title or keyword in book.author:
                # SEARCH命令：状态显示为Borrowed/Available（不带借阅者ID）
                status = "Borrowed" if book.is_borrowed else "Available"
                results.append(f'{book.isbn} "{book.title}" by {book.author} - {status}')
        return results

    def list_available_books(self):
        """列出可借图书"""
        results = []
        for book in self.books.values():
            if not book.is_borrowed:
                # LIST_AVAILABLE命令：状态显示为Available
                results.append(f'{book.isbn} "{book.title}" by {book.author} - Available')
        return results

    def list_borrowed_books(self):
        """列出已借出图书"""
        results = []
        for book in self.books.values():
            if book.is_borrowed:
                # LIST_BORROWED命令：状态显示为Borrowed by [借阅者ID]
                results.append(f'{book.isbn} "{book.title}" by {book.author} - Borrowed by {book.current_borrower}')
        return results

    def get_borrow_history(self, borrower_id):
        """获取借阅历史"""
        history = []
        for record_id in self.borrower_records.get(borrower_id, []):
            record = self.borrow_records[record_id]
            history.append(f"{record.record_id}: {record.book_isbn} borrowed on {record.borrow_date} returned on {record.return_date}")
        return history


class LibraryManagementSystem:
    """图书馆管理系统主类"""
    def __init__(self):
        self.library = Library()

    def process_command(self, command):
        """处理命令"""
        parts = command.strip().split()
        if not parts:
            return ""
        cmd = parts[0]
        try:
            if cmd == "ADD_BOOK":
                if len(parts) < 4:
                    return "Error: ADD_BOOK command requires at least 3 arguments"
                isbn = parts[1]
                # 处理带引号的标题
                title_parts = []
                i = 2
                while i < len(parts) and parts[2].startswith('"') and not parts[i].endswith('"'):
                    i += 1
                title = ' '.join(parts[2:i+1]).strip('"')
                author = ' '.join(parts[i+1:]) if len(parts) > i+1 else "Unknown"
                success, message = self.library.add_book(isbn, title, author)
                return message

            elif cmd == "REMOVE_BOOK":
                if len(parts) != 2:
                    return "Error: REMOVE_BOOK command requires 1 argument"
                isbn = parts[1]
                success, message = self.library.remove_book(isbn)
                return message

            elif cmd == "BORROW":
                if len(parts) != 4:
                    return "Error: BORROW command requires 3 arguments"
                isbn = parts[1]
                borrower_id = parts[2]
                borrow_date = parts[3]
                success, message = self.library.borrow_book(isbn, borrower_id, borrow_date)
                return message

            elif cmd == "RETURN":
                if len(parts) != 4:
                    return "Error: RETURN command requires 3 arguments"
                isbn = parts[1]
                borrower_id = parts[2]
                return_date = parts[3]
                success, message = self.library.return_book(isbn, borrower_id, return_date)
                return message

            elif cmd == "SEARCH":
                if len(parts) < 2:
                    return "Error: SEARCH command requires at least 1 argument"
                keyword = ' '.join(parts[1:])
                results = self.library.search_books(keyword)
                return '\n'.join(results) if results else "No books found"

            elif cmd == "LIST_AVAILABLE":
                results = self.library.list_available_books()
                return '\n'.join(results) if results else "No available books"

            elif cmd == "LIST_BORROWED":
                results = self.library.list_borrowed_books()
                return '\n'.join(results) if results else "No borrowed books"

            elif cmd == "HISTORY":
                if len(parts) != 2:
                    return "Error: HISTORY command requires 1 argument"
                borrower_id = parts[1]
                history = self.library.get_borrow_history(borrower_id)
                return '\n'.join(history) if history else "No borrow history"

            elif cmd == "EXIT":
                return "EXIT"

            else:
                return f"Error: Unknown command {cmd}"
        except Exception as e:
            return f"Error: {str(e)}"


def main():
    """主函数"""
    system = LibraryManagementSystem()
    while True:
        try:
            line = input().strip()
            if not line:
                continue
            result = system.process_command(line)
            if result == "EXIT":
                break
            if result:  # 只输出非空结果
                print(result)
        except EOFError:
            break


if __name__ == "__main__":
    main()