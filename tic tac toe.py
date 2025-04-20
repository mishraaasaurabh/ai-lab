import random

def print_board(board):
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")

def check_winner(board, player):
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
        (0, 4, 8), (2, 4, 6)               # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combinations)

def is_full(board):
    return ' ' not in board

def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter position (0-8): "))
            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = player
                break
            else:
                print("Invalid move! Try again.")
        except:
            print("Enter a number between 0 and 8.")

def ai_move(board):
    # Simple AI that picks a random empty spot
    empty = [i for i, spot in enumerate(board) if spot == ' ']
    move = random.choice(empty)
    board[move] = 'O'
    print(f"AI chooses position {move}")

def play_game(vs_ai=False):
    board = [' '] * 9
    current_player = 'X'

    print("Welcome to Tic Tac Toe!")
    print("Positions:")
    print(" 0 | 1 | 2 ")
    print("---+---+---")
    print(" 3 | 4 | 5 ")
    print("---+---+---")
    print(" 6 | 7 | 8 \n")

    while True:
        print_board(board)

        if current_player == 'X' or not vs_ai:
            player_move(board, current_player)
        else:
            ai_move(board)

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

# Game entry point
if __name__ == "__main__":
    mode = input("Play vs AI? (y/n): ").lower()
    play_game(vs_ai=(mode == 'y'))
