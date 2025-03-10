def print_board(board):

    print("\n---------")
    for row in board:
        print("| " + " | ".join(row) + " |")
    print("---------\n")

def check_win(board, player):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def is_board_full(board):

    for row in board:
        if " " in row:
            return False
    return True

def get_move(player):

    while True:
        move = input(f"player {player}, enter your move (row and column, e.g., 1 2): ")
        try:
            row, col = map(int, move.split())
            if row in [1, 2, 3] and col in [1, 2, 3]:
                return row - 1, col - 1
            else:
                print("invalid input: row and column must be between 1 and 3.")
        except ValueError:
            print("invalid input: please enter two numbers separated by a space.")

def main():
    # Initialize an empty 3x3 board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row, col = get_move(current_player)

        # Check if the chosen cell is already occupied
        if board[row][col] != " ":
            print("cell taken. try a different move.")
            continue

        # Update the board with the current player's move
        board[row][col] = current_player

        # Check for a win or tie
        if check_win(board, current_player):
            print_board(board)
            print(f"congratulations! player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("it's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
