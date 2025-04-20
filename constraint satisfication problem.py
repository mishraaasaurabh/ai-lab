# Define the CSP problem: Map coloring
class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables        # List of variables (regions)
        self.domains = domains            # Domains for each variable (color options)
        self.constraints = constraints    # List of constraints (adjacency restrictions)
        self.assignment = {}              # Initial empty assignment

    def is_consistent(self, variable, value):
        """
        Check if the current assignment is consistent with the constraints.
        """
        for neighbor in self.constraints.get(variable, []):
            if neighbor in self.assignment and self.assignment[neighbor] == value:
                return False
        return True

    def backtrack(self):
        """
        Backtracking algorithm to solve the CSP.
        """
        # If all variables are assigned, return the current assignment (solution)
        if len(self.assignment) == len(self.variables):
            return self.assignment

        # Select the next unassigned variable
        unassigned_variables = [v for v in self.variables if v not in self.assignment]
        variable = unassigned_variables[0]  # Choose the first unassigned variable (you could use heuristics here)

        # Try all values in the domain of the selected variable
        for value in self.domains[variable]:
            if self.is_consistent(variable, value):
                # Assign the value to the variable
                self.assignment[variable] = value
                result = self.backtrack()
                if result:
                    return result
                # If no result, backtrack (remove the assignment)
                del self.assignment[variable]

        return None

# Define the Map Coloring problem
def map_coloring():
    # Variables (regions)
    variables = ['A', 'B', 'C']

    # Domains (colors for each region)
    domains = {
        'A': ['Red', 'Green', 'Blue'],
        'B': ['Red', 'Green', 'Blue'],
        'C': ['Red', 'Green', 'Blue'],
    }

    # Constraints (no two adjacent regions should have the same color)
    constraints = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B'],
    }

    # Create the CSP solver
    csp = CSP(variables, domains, constraints)

    # Solve the CSP using backtracking
    solution = csp.backtrack()

    if solution:
        print("Solution found:")
        for variable, value in solution.items():
            print(f"Region {variable} is colored {value}")
    else:
        print("No solution found.")

# Run the map coloring example
if __name__ == "__main__":
    map_coloring()
