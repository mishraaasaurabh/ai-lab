import heapq
import matplotlib.pyplot as plt

# Define coordinates (heuristic estimation will use Euclidean distance)
city_coords = {
    "A": (0, 0),
    "B": (2, 4),
    "C": (5, 2),
    "D": (6, 6),
    "E": (8, 3),
    "F": (10, 0)
}

# Define connections and distances between cities
city_graph = {
    "A": [("B", 5), ("C", 6)],
    "B": [("A", 5), ("D", 5)],
    "C": [("A", 6), ("D", 4), ("E", 3)],
    "D": [("B", 5), ("C", 4), ("E", 2)],
    "E": [("C", 3), ("D", 2), ("F", 5)],
    "F": [("E", 5)]
}

# Heuristic: straight-line distance to goal
def heuristic(a, b):
    x1, y1 = city_coords[a]
    x2, y2 = city_coords[b]
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def best_first_search(start, goal):
    visited = set()
    queue = [(heuristic(start, goal), start, [start])]

    while queue:
        _, current, path = heapq.heappop(queue)

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        for neighbor, _ in city_graph[current]:
            if neighbor not in visited:
                heapq.heappush(queue, (heuristic(neighbor, goal), neighbor, path + [neighbor]))

    return None

def a_star_search(start, goal):
    visited = set()
    queue = [(heuristic(start, goal), 0, start, [start])]

    while queue:
        est_total, cost_so_far, current, path = heapq.heappop(queue)

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        for neighbor, weight in city_graph[current]:
            if neighbor not in visited:
                new_cost = cost_so_far + weight
                est = new_cost + heuristic(neighbor, goal)
                heapq.heappush(queue, (est, new_cost, neighbor, path + [neighbor]))

    return None

def visualize_path(path, title="Path"):
    plt.figure(figsize=(8, 6))
    for city, (x, y) in city_coords.items():
        plt.plot(x, y, 'ko')
        plt.text(x + 0.2, y + 0.2, city, fontsize=12)

    for city, neighbors in city_graph.items():
        for neighbor, _ in neighbors:
            x1, y1 = city_coords[city]
            x2, y2 = city_coords[neighbor]
            plt.plot([x1, x2], [y1, y2], 'gray')

    if path:
        px, py = zip(*[city_coords[city] for city in path])
        plt.plot(px, py, 'ro-', label='Path')
        plt.title(title)
        plt.legend()

    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

if __name__ == "__main__":
    start = "A"
    goal = "F"

    bfs_path = best_first_search(start, goal)
    astar_path = a_star_search(start, goal)

    print("Best-First Search Path:", bfs_path)
    print("A* Search Path:", astar_path)

    visualize_path(bfs_path, "Best-First Search")
    visualize_path(astar_path, "A* Search")
