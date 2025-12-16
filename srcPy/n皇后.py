from typing import List

result = []


def check(board: List[int], x: int) -> bool:
    """检查皇后摆放位置是否合法。

    Args:
        board: 当前已摆放皇后的位置列表（每项为列号，索引为行号）。
        x: 当前要摆放皇后的列号。

    Returns:
        如果位置冲突返回 True，否则返回 False。
    """
    y = len(board)
    for i in range(y):
        if abs(board[i] - x) in (0, y-i):
            return True

    return False


def queens(num: int = 8, board: List[int] = []) -> None:
    """ 八皇后问题求解
    Args:
        num: 皇后数量及棋盘大小（num x num）。
        board: 当前已摆放皇后的位置列表。
    Returns:
        结果存储在全局变量 result 中。
    """
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
