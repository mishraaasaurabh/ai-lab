from collections import deque

# Helper functions
def print_state(state):
    for i, stack in enumerate(state):
        print(f"Stack {i}: {stack}")
    print()

def is_goal_state(state, goal):
    return state == goal

def get_possible_actions(state):
    actions = []
    for i, stack1 in enumerate(state):
        if len(stack1) == 0:
            continue
        # Pick top block from stack1
        top_block = stack1[-1]
        for j, stack2 in enumerate(state):
            if i != j and (len(stack2) == 0 or stack2[-1] != top_block):
                # Create a new state where we move the top block from stack1 to stack2
                new_state = [list(stack) for stack in state]
                new_state[i].pop()  # Remove block from stack1
                new_state[j].append(top_block)  # Add block to stack2
                actions.append(('Move', top_block, i, j, new_state))
    return actions

def bfs_block_world(initial_state, goal_state):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        
        # Check if goal is reached
        if is_goal_state(current_state, goal_state):
            return path + [current_state]

        visited.add(tuple(map(tuple, current_state)))

        # Get possible actions
        for action in get_possible_actions(current_state):
            _, block, from_stack, to_stack, next_state = action
            state_tuple = tuple(map(tuple, next_state))
            if state_tuple not in visited:
                queue.append((next_state, path + [(block, from_stack, to_stack)]))

    return None

# Example usage
if __name__ == "__main__":
    # Initial state: [['A', 'B'], ['C'], []]
    initial_state = [['A', 'B'], ['C'], []]
    # Goal state: [['C'], ['A', 'B'], []]
    goal_state = [['C'], ['A', 'B'], []]

    # Solve the problem
    solution = bfs_block_world(initial_state, goal_state)

    if solution:
        print("Solution found! Steps:")
        for step in solution:
            print(f"Move block {step[0]} from Stack {step[1]} to Stack {step[2]}")
    else:
        print("No solution found.")
