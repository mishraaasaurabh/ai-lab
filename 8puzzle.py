import heapq

GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

MOVES = [
    (-3, 'Up'),
    (3, 'Down'),
    (-1, 'Left'),
    (1, 'Right')
]

def manhattan_distance(state):
    distance = 0
    for i in range(9):
        value = state[i]
        if value != 0:
            goal_index = GOAL_STATE.index(value)
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_index, 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def generate_moves(state):
    index = state.index(0)
    row, col = divmod(index, 3)
    neighbors = []

    for move, direction in MOVES:
        new_index = index + move
        if 0 <= new_index < 9:
            # Prevent wrap-around from left/right edges
            if abs(index - new_index) == 1 and row != new_index // 3:
                continue
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append((tuple(new_state), direction))

    return neighbors

def a_star(start_state):
    open_set = []
    heapq.heappush(open_set, (manhattan_distance(start_state), 0, start_state, []))
    visited = set()

    while open_set:
        f, g, state, path = heapq.heappop(open_set)

        if state == GOAL_STATE:
            return path

        visited.add(state)

        for neighbor, direction in generate_moves(state):
            if neighbor not in visited:
                heapq.heappush(open_set, (g + 1 + manhattan_distance(neighbor), g + 1, neighbor, path + [direction]))

    return None

def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])

if __name__ == "__main__":
    start_state = (1, 2, 3,
                   4, 0, 6,
                   7, 5, 8)

    print("Start State:")
    print_state(start_state)

    path = a_star(start_state)

    if path:
        print("\nSolution found!")
        print("Steps to goal:")
        print(" -> ".join(path))
    else:
        print("\nNo solution found.")
