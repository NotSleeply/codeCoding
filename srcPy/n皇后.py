result = []


def check(board, x) -> bool:
    """检查皇后摆放位置是否合法"""
    for i in range(len(board)):
        if abs(board[i] - x) == abs(i - len(board)) or board[i] == x:
            return True

    return False


def queens(num=8, board=[]) -> None:
    """八皇后问题求解"""
    for col in range(num):
        if not check(board, col):
            board = board + [col]
            if len(board) == num:
                result.append(board)
            else:
                queens(num, board)
                board = board[:-1]


def main() -> None:
    """主函数"""
    queens(4)
    '''
    [1, 3, 0, 2]
    [2, 0, 3, 1]
    '''
    for i in result:
        print(i)


if __name__ == "__main__":
    main()
