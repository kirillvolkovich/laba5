def print_board(board):
    print("---------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print("\n---------")


def check_win(board, player):
    for i in range(3):
        if board[i] == [player, player, player] or \
                [board[0][i], board[1][i], board[2][i]] == [player, player, player] or \
                [board[0][0], board[1][1], board[2][2]] == [player, player, player] or \
                [board[0][2], board[1][1], board[2][0]] == [player, player, player]:
            return True
    return False


def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    print_board(board)

    players = ["X", "O"]
    current_player = players[0]

    while True:
        row = int(input(f"Игрок {current_player}, выберите строку (1-3): ")) - 1
        col = int(input(f"Игрок {current_player}, выберите столбец (1-3): ")) - 1

        if board[row][col] != " ":
            print("Эта клетака занята")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_win(board, current_player):
            print(f"Игрок {current_player} выиграл")
            break
        elif " " not in [cell for row in board for cell in row]:
            print("Ничья")
            break

        current_player = players[1] if current_player == players[0] else players[0]

play_game()

