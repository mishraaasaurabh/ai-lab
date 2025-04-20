import math
import random
import matplotlib.pyplot as plt

# The objective function
def objective(x):
    return math.sin(x) + math.cos(2 * x)

# Hill Climbing algorithm
def hill_climb(start, step_size=0.01, max_iterations=1000):
    current_x = start
    current_score = objective(current_x)
    path = [(current_x, current_score)]

    for _ in range(max_iterations):
        # Check small changes in both directions
        neighbors = [current_x + step_size, current_x - step_size]
        neighbor_scores = [objective(n) for n in neighbors]

        best_index = neighbor_scores.index(max(neighbor_scores))
        best_neighbor = neighbors[best_index]
        best_score = neighbor_scores[best_index]

        if best_score > current_score:
            current_x, current_score = best_neighbor, best_score
            path.append((current_x, current_score))
        else:
            break  # Local maximum reached

    return current_x, current_score, path

# Visualization
def plot_function_and_path(path, func, xmin=0, xmax=10):
    x_vals = [x / 100.0 for x in range(int(xmin*100), int(xmax*100))]
    y_vals = [func(x) for x in x_vals]

    path_x = [p[0] for p in path]
    path_y = [p[1] for p in path]

    plt.figure(figsize=(10, 5))
    plt.plot(x_vals, y_vals, label='f(x) = sin(x) + cos(2x)')
    plt.plot(path_x, path_y, 'ro-', label='Hill Climb Path')
    plt.title('Hill Climbing Optimization')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Run the algorithm
if __name__ == "__main__":
    start_x = random.uniform(0, 10)
    peak_x, peak_val, path = hill_climb(start_x)
    
    print(f"Start at x = {start_x:.4f}")
    print(f"Reached peak at x = {peak_x:.4f} with value = {peak_val:.4f}")
    
    plot_function_and_path(path, objective)
