import math

def create_board():
    return [' ' for _ in range(9)]

def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")
    print()

def check_winner(board, player):
    win_states = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(all(board[i] == player for i in combo) for combo in win_states)

def is_full(board):
    return ' ' not in board

# Alpha-Beta Minimax
def alphabeta(board, depth, alpha, beta, is_maximizing):
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = alphabeta(board, depth + 1, alpha, beta, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Beta cutoff
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = alphabeta(board, depth + 1, alpha, beta, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha cutoff
        return min_eval

# Find best move for AI using alpha-beta pruning
def best_move_ab(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = alphabeta(board, 0, -math.inf, math.inf, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Main game loop
def play_game():
    board = create_board()
    current_player = 'O'

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
            move = best_move_ab(board)
            print(f"AI plays at {move}")

        board[move] = current_player
        current_player = 'X' if current_player == 'O' else 'O'

if __name__ == "__main__":
    play_game()
