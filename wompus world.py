import random
import math
import itertools
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


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
        self.grid = np.zeros((GRID_SIZE, GRID_SIZE))  # Empty grid
        self.wumpus = WUMPUS_POSITION
        self.pit = PIT_POSITION
        self.gold = GOLD_POSITION
        self.agent_position = START_POSITION
        self.agent_direction = 'UP'
        
        # Set the Wumpus, pit, and gold in the grid
        self.grid[WUMPUS_POSITION] = 1  # Wumpus
        self.grid[PIT_POSITION] = -1  # Pit
        self.grid[GOLD_POSITION] = 2  # Gold

    def is_valid_move(self, new_position):
        """Check if a move is valid (not out of bounds and no danger)"""
        if new_position[0] < 0 or new_position[0] >= GRID_SIZE or new_position[1] < 0 or new_position[1] >= GRID_SIZE:
            return False
        if new_position == self.pit or new_position == self.wumpus:
            return False
        return True

    def move(self):
        """Randomly move the agent to a new position"""
        possible_moves = []
        if self.is_valid_move((self.agent_position[0] - 1, self.agent_position[1])):
            possible_moves.append('UP')
        if self.is_valid_move((self.agent_position[0] + 1, self.agent_position[1])):
            possible_moves.append('DOWN')
        if self.is_valid_move((self.agent_position[0], self.agent_position[1] - 1)):
            possible_moves.append('LEFT')
        if self.is_valid_move((self.agent_position[0], self.agent_position[1] + 1)):
            possible_moves.append('RIGHT')

        if not possible_moves:
            return False  # No valid moves

        move = random.choice(possible_moves)
        if move == 'UP':
            self.agent_position = (self.agent_position[0] - 1, self.agent_position[1])
        elif move == 'DOWN':
            self.agent_position = (self.agent_position[0] + 1, self.agent_position[1])
        elif move == 'LEFT':
            self.agent_position = (self.agent_position[0], self.agent_position[1] - 1)
        elif move == 'RIGHT':
            self.agent_position = (self.agent_position[0], self.agent_position[1] + 1)

        return True

    def is_goal_reached(self):
        """Check if the agent reached the gold"""
        return self.agent_position == self.gold

    def is_dead(self):
        """Check if the agent encountered the Wumpus or fell into a pit"""
        return self.agent_position == self.wumpus or self.agent_position == self.pit

# Brute Force Pathfinding
def brute_force_search(wumpus_world):
    """Generate all possible paths and check for the best path (Brute Force)"""
    all_positions = list(itertools.product(range(GRID_SIZE), repeat=2))  # all possible positions
    possible_paths = list(itertools.permutations(all_positions))  # all possible paths
    best_path = None
    for path in possible_paths:
        # Check if path is valid
        for position in path:
            if not wumpus_world.is_valid_move(position):
                break
        else:
            best_path = path
            break
    return best_path

# Simulated Annealing for Wumpus World
class SimulatedAnnealingWumpus:
    def __init__(self, wumpus_world, initial_temp=1000, temp_decay=0.995, stopping_temp=1e-3, max_iterations=10000):
        self.wumpus_world = wumpus_world
        self.temperature = initial_temp
        self.temp_decay = temp_decay
        self.stopping_temp = stopping_temp
        self.max_iterations = max_iterations

    def generate_new_state(self):
        """Generate a random new state by making a move"""
        return self.wumpus_world.move()

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
            if self.accept_solution(new_state):
                if self.wumpus_world.is_goal_reached():
                    return True  # Goal reached
            # Cool down the temperature
            self.temperature *= self.temp_decay
            iteration += 1
        return False

# Main execution
if __name__ == "__main__":
    wumpus_world = WumpusWorld()
    
    # Brute Force Search
    best_path = brute_force_search(wumpus_world)
    print(f"Best Path (Brute Force): {best_path}")
    
    # Simulated Annealing Search
    sa_solver = SimulatedAnnealingWumpus(wumpus_world)
    goal_reached = sa_solver.run()
    print(f"Simulated Annealing - Goal Reached: {goal_reached}")
