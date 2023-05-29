def solve_queens(board, col=0):
    if col >= 8:
        return [board]

    solutions = []
    for row in range(8):
        if is_valid(board, row, col):
            board[row][col] = 1
            solutions += solve_queens(board, col + 1)
            board[row][col] = 0

    return solutions


def is_valid(board, row, col):
    for i in range(8):
        if board[row][i] == 1 or board[i][col] == 1:
            return False
    for i in range(8):
        for j in range(8):
            if (i + j == row + col) or (i - j == row - col):
                if board[i][j] == 1:
                    return False
    return True


board = [[0] * 8 for _ in range(8)]
solutions = solve_queens(board)
print('Возможное количество расстановок', len(solutions))

