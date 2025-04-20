from collections import deque

# Possible locations
LOCATIONS = ['door', 'middle', 'window']

# Initial and goal states
initial_state = ('door', 'window', False, False)
goal_state = ('middle', 'middle', True, True)

def is_goal(state):
    return state == goal_state

def get_successors(state):
    monkey, box, on_box, has_banana = state
    successors = []

    # Monkey walks
    for loc in LOCATIONS:
        if loc != monkey:
            successors.append((loc, box, False, has_banana))  # stepping down if was on box

    # Push box (only if monkey and box at same location and not on box)
    if monkey == box and not on_box:
        for loc in LOCATIONS:
            if loc != box:
                successors.append((loc, loc, False, has_banana))

    # Climb box
    if monkey == box and not on_box:
        successors.append((monkey, box, True, has_banana))

    # Grab banana
    if monkey == 'middle' and box == 'middle' and on_box and not has_banana:
        successors.append((monkey, box, on_box, True))

    return successors

def bfs_monkey_banana():
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        if current in visited:
            continue
        visited.add(current)

        if is_goal(current):
            return path + [current]

        for successor in get_successors(current):
            queue.append((successor, path + [current]))

    return None

# Run it
if __name__ == "__main__":
    solution = bfs_monkey_banana()
    if solution:
        print("Monkey can get the banana. Steps:")
        for step in solution:
            print(f"Monkey at: {step[0]}, Box at: {step[1]}, On box: {step[2]}, Has banana: {step[3]}")
    else:
        print("No solution found.")
