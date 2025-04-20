import random
import math

# Define the Wumpus World grid and elements
GRID_SIZE = 4
WUMPUS_POSITION = (2, 2)
PIT_POSITION = (1, 3)
GOLD_POSITION = (3, 0)
START_POSITION = (0, 0)

# Directions: Up, Right, Down, Left
DIRECTIONS = ['UP', 'RIGHT', 'DOWN', 'LEFT']

# Define a simple grid environment
class WumpusWorld:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]  # Empty grid
        self.wumpus = WUMPUS_POSITION
        self.pit = PIT_POSITION
        self.gold = GOLD_POSITION
        self.agent_position = START_POSITION
        
        # Set the Wumpus, pit, and gold in the grid
        self.grid[WUMPUS_POSITION[0]][WUMPUS_POSITION[1]] = 1  # Wumpus
        self.grid[PIT_POSITION[0]][PIT_POSITION[1]] = -1  # Pit
        self.grid[GOLD_POSITION[0]][GOLD_POSITION[1]] = 2  # Gold

    def is_valid_move(self, new_position):
        """Check if a move is valid (not out of bounds and no danger)"""
        if new_position[0] < 0 or new_position[0] >= GRID_SIZE or new_position[1] < 0 or new_position[1] >= GRID_SIZE:
            return False
        if new_position == self.pit or new_position == self.wumpus:
            return False
        return True

    def is_goal_reached(self):
        """Check if the agent reached the gold"""
        return self.agent_position == self.gold

    def is_dead(self):
        """Check if the agent encountered the Wumpus or fell into a pit"""
        return self.agent_position == self.wumpus or self.agent_position == self.pit

    def get_possible_moves(self):
        """Returns a list of valid moves from the current position"""
        possible_moves = []
        current_position = self.agent_position
        if self.is_valid_move((current_position[0] - 1, current_position[1])):
            possible_moves.append('UP')
        if self.is_valid_move((current_position[0] + 1, current_position[1])):
            possible_moves.append('DOWN')
        if self.is_valid_move((current_position[0], current_position[1] - 1)):
            possible_moves.append('LEFT')
        if self.is_valid_move((current_position[0], current_position[1] + 1)):
            possible_moves.append('RIGHT')
        return possible_moves


# Depth First Search (DFS) for Brute Force Pathfinding (Optimized)
def dfs(wumpus_world, current_position, visited, path):
    """Perform DFS to find the path to the goal"""
    if wumpus_world.is_goal_reached():
        return path

    visited.add(current_position)
    possible_moves = wumpus_world.get_possible_moves()

    for move in possible_moves:
        if move == 'UP':
            new_position = (current_position[0] - 1, current_position[1])
        elif move == 'DOWN':
            new_position = (current_position[0] + 1, current_position[1])
        elif move == 'LEFT':
            new_position = (current_position[0], current_position[1] - 1)
        elif move == 'RIGHT':
            new_position = (current_position[0], current_position[1] + 1)

        if new_position not in visited:
            path.append(new_position)
            wumpus_world.agent_position = new_position
            result = dfs(wumpus_world, new_position, visited, path)
            if result:
                return result
            path.pop()  # Backtrack if we hit a dead end

    return None  # No valid path found

# Simulated Annealing for Wumpus World (Optimized)
class SimulatedAnnealingWumpus:
    def __init__(self, wumpus_world, initial_temp=1000, temp_decay=0.995, stopping_temp=1e-3, max_iterations=10000):
        self.wumpus_world = wumpus_world
        self.temperature = initial_temp
        self.temp_decay = temp_decay
        self.stopping_temp = stopping_temp
        self.max_iterations = max_iterations

    def generate_new_state(self):
        """Generate a random new state by making a move"""
        possible_moves = self.wumpus_world.get_possible_moves()
        if not possible_moves:
            return False
        move = random.choice(possible_moves)

        if move == 'UP':
            self.wumpus_world.agent_position = (self.wumpus_world.agent_position[0] - 1, self.wumpus_world.agent_position[1])
        elif move == 'DOWN':
            self.wumpus_world.agent_position = (self.wumpus_world.agent_position[0] + 1, self.wumpus_world.agent_position[1])
        elif move == 'LEFT':
            self.wumpus_world.agent_position = (self.wumpus_world.agent_position[0], self.wumpus_world.agent_position[1] - 1)
        elif move == 'RIGHT':
            self.wumpus_world.agent_position = (self.wumpus_world.agent_position[0], self.wumpus_world.agent_position[1] + 1)

        return True

    def accept_solution(self, new_state):
        """Accept the new state based on the temperature"""
        if not self.wumpus_world.is_dead():
            return True
        return random.random() < math.exp(-self.temperature)

    def run(self):
        """Run the simulated annealing algorithm"""
        iteration = 0
        while self.temperature > self.stopping_temp and iteration < self.max_iterations:
            new_state = self.generate_new_state()
            if new_state and self.accept_solution(new_state):
                if self.wumpus_world.is_goal_reached():
                    return True  # Goal reached
            # Cool down the temperature
            self.temperature *= self.temp_decay
            iteration += 1
        return False


# Main execution
if __name__ == "__main__":
    # Initialize Wumpus World
    wumpus_world = WumpusWorld()
    
    # Optimized DFS for Brute Force Search
    visited = set()
    initial_position = wumpus_world.agent_position
    path = [initial_position]
    found_path = dfs(wumpus_world, initial_position, visited, path)
    if found_path:
        print(f"Path found (Brute Force - DFS): {found_path}")
    else:
        print("No valid path found using DFS.")

    # Simulated Annealing Search
    sa_solver = SimulatedAnnealingWumpus(wumpus_world)
    goal_reached = sa_solver.run()
    print(f"Simulated Annealing - Goal Reached: {goal_reached}")
