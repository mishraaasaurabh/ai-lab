import math

# Initialize board
def create_board():
    return [' ' for _ in range(9)]

# Display board
def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")
    print()

# Check for winner
def check_winner(board, player):
    win_states = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_states)

def is_full(board):
    return ' ' not in board

# Minimax Algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Best move for AI
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Main game loop (human = O, AI = X)
def play_game():
    board = create_board()
    current_player = 'O'  # Human starts

    while True:
        print_board(board)

        if check_winner(board, 'X'):
            print("AI wins!")
            break
        elif check_winner(board, 'O'):
            print("You win!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        if current_player == 'O':
            try:
                move = int(input("Enter your move (0-8): "))
                if board[move] != ' ':
                    print("Invalid move. Try again.")
                    continue
            except:
                print("Please enter a number from 0 to 8.")
                continue
        else:
            move = best_move(board)
            print(f"AI plays at {move}")

        board[move] = current_player
        current_player = 'X' if current_player == 'O' else 'O'

if __name__ == "__main__":
    play_game()
