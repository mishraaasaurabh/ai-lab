from collections import deque

def is_goal(state, goal):
    return goal in state

def get_successors(state, capacities):
    a, b = state
    cap_a, cap_b = capacities
    successors = set()

    # Fill either jug
    successors.add((cap_a, b))
    successors.add((a, cap_b))

    # Empty either jug
    successors.add((0, b))
    successors.add((a, 0))

    # Pour A -> B
    transfer = min(a, cap_b - b)
    successors.add((a - transfer, b + transfer))

    # Pour B -> A
    transfer = min(b, cap_a - a)
    successors.add((a + transfer, b - transfer))

    return successors

def bfs_water_jug(capacities, goal):
    start = (0, 0)
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (current, path) = queue.popleft()
        if current in visited:
            continue
        visited.add(current)

        if is_goal(current, goal):
            return path + [current]

        for successor in get_successors(current, capacities):
            if successor not in visited:
                queue.append((successor, path + [current]))
    
    return None

# Example usage
if __name__ == "__main__":
    capacities = (4, 3)  # Jug A: 4L, Jug B: 3L
    goal = 2
    solution = bfs_water_jug(capacities, goal)

    if solution:
        print("Solution steps:")
        for step in solution:
            print(f"Jug A: {step[0]}L, Jug B: {step[1]}L")
    else:
        print("No solution found.")
