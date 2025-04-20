import matplotlib.pyplot as plt
import networkx as nx
import itertools
import numpy as np

class TSP:
    def __init__(self, cities):
        self.cities = cities  # List of city coordinates (x, y)
        self.G = nx.Graph()  # Graph for visualization
        self.create_graph()

    def create_graph(self):
        # Add cities (nodes) to the graph
        for i, city in enumerate(self.cities):
            self.G.add_node(i, pos=city)

        # Add edges with distances
        for i in range(len(self.cities)):
            for j in range(i + 1, len(self.cities)):
                distance = self.euclidean_distance(self.cities[i], self.cities[j])
                self.G.add_edge(i, j, weight=distance)

    def euclidean_distance(self, city1, city2):
        # Calculate Euclidean distance between two cities (x1, y1) and (x2, y2)
        return np.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

    def calculate_total_distance(self, route):
        # Calculate the total distance of a given route
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += self.G[route[i]][route[i + 1]]['weight']
        total_distance += self.G[route[-1]][route[0]]['weight']  # Closing the loop (back to start)
        return total_distance

    def find_shortest_route(self):
        # Generate all possible routes (permutations)
        all_permutations = itertools.permutations(range(len(self.cities)))
        shortest_route = None
        min_distance = float('inf')

        for route in all_permutations:
            distance = self.calculate_total_distance(route)
            if distance < min_distance:
                min_distance = distance
                shortest_route = route

        return shortest_route, min_distance

    def draw_graph(self, shortest_route=None):
        # Visualize the graph and the shortest route (if found)
        pos = nx.get_node_attributes(self.G, 'pos')
        plt.figure(figsize=(8, 6))
        nx.draw(self.G, pos, with_labels=True, node_size=700, font_size=12, node_color='skyblue', edge_color='gray')

        if shortest_route:
            # Highlight the shortest route
            path_edges = [(shortest_route[i], shortest_route[i + 1]) for i in range(len(shortest_route) - 1)]
            path_edges.append((shortest_route[-1], shortest_route[0]))  # Closing the loop
            nx.draw_networkx_edges(self.G, pos, edgelist=path_edges, edge_color='red', width=2)

        plt.title("Traveling Salesman Problem (TSP)")
        plt.show()


# Example usage
if __name__ == "__main__":
    # List of cities with coordinates (x, y)
    cities = [(0, 0), (1, 3), (4, 3), (6, 1), (5, 0), (2, 1)]

    tsp_solver = TSP(cities)
    
    # Find the shortest route using brute force (permutation)
    shortest_route, min_distance = tsp_solver.find_shortest_route()

    print("Shortest Route:", shortest_route)
    print("Minimum Distance:", min_distance)

    # Visualize the graph and the shortest route
    tsp_solver.draw_graph(shortest_route)
