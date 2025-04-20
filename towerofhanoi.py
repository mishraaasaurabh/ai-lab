def tower_of_hanoi(n, source, auxiliary, target, steps=None):
    if steps is None:
        steps = []

    if n == 1:
        steps.append((source, target))
    else:
        tower_of_hanoi(n - 1, source, target, auxiliary, steps)
        steps.append((source, target))
        tower_of_hanoi(n - 1, auxiliary, source, target, steps)

    return steps

def print_steps(steps):
    for i, step in enumerate(steps, 1):
        print(f"Step {i}: Move disk from {step[0]} to {step[1]}")

if __name__ == "__main__":
    n = 3  # Number of disks
    steps = tower_of_hanoi(n, 'A', 'B', 'C')
    print(f"\nTotal moves required: {len(steps)}")
    print_steps(steps)
