import matplotlib.pyplot as plt

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n, row=0, board=None, solutions=None):
    if board is None:
        board = [-1] * n
    if solutions is None:
        solutions = []

    if row == n:
        solutions.append(board[:])
        return solutions

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens(n, row + 1, board, solutions)
            board[row] = -1

    return solutions

def print_board(board):
    n = len(board)
    for row in range(n):
        line = ['.'] * n
        if board[row] != -1:
            line[board[row]] = 'Q'
        print(" ".join(line))
    print()

def visualize_board(board):
    n = len(board)
    fig, ax = plt.subplots()
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_aspect('equal')
    ax.set_title("8-Queens Solution")

    # Draw the board squares
    for i in range(n):
        for j in range(n):
            color = '#EEE' if (i + j) % 2 == 0 else '#999'
            rect = plt.Rectangle((j, n - i - 1), 1, 1, facecolor=color)
            ax.add_patch(rect)

    # Place queens
    for i in range(n):
        ax.text(board[i] + 0.5, n - i - 0.5, '♛', fontsize=30, ha='center', va='center', color='black')

    # plt.show()

if __name__ == "__main__":
    N = 8
    solutions = solve_n_queens(N)

    if solutions:
        print("One valid solution:\n")
        print_board(solutions[0])
        visualize_board(solutions[0])
    else:
        print("No solution found.")
