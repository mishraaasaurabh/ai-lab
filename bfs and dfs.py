import matplotlib.pyplot as plt
import networkx as nx
from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # adjacency list
        self.G = nx.DiGraph()  # directed graph for visualization

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.G.add_edge(u, v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend([n for n in self.graph[vertex] if n not in visited])
        return result

    def dfs(self, start):
        visited = set()
        result = []

        def dfs_recursive(v):
            visited.add(v)
            result.append(v)
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return result

    def draw_graph(self, traversal_order=None, title="Graph", color='lightblue'):
        pos = nx.spring_layout(self.G)
        node_colors = []

        for node in self.G.nodes():
            if traversal_order and node in traversal_order:
                idx = traversal_order.index(node)
                node_colors.append(plt.cm.viridis(idx / len(traversal_order)))
            else:
                node_colors.append(color)

        plt.figure(figsize=(8, 6))
        nx.draw(self.G, pos, with_labels=True, node_color=node_colors, edge_color='gray', node_size=800, font_size=14)
        if traversal_order:
            path_edges = list(zip(traversal_order, traversal_order[1:]))
            nx.draw_networkx_edges(self.G, pos, edgelist=path_edges, edge_color='red', width=2)
        plt.title(title)
        plt.show()

# Example usage
if __name__ == "__main__":
    g = Graph()
    edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
    for u, v in edges:
        g.add_edge(u, v)

    start_node = 2
    bfs_result = g.bfs(start_node)
    dfs_result = g.dfs(start_node)

    print("BFS Order:", bfs_result)
    print("DFS Order:", dfs_result)

    g.draw_graph(bfs_result, title="BFS Traversal")
    g.draw_graph(dfs_result, title="DFS Traversal")
