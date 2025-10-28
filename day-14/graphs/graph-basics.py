'''
Graph can be represented in two ways

    - Adjecency Matrix (2D array)
    - Adjecency List (Dictionary of Lists)

'''

class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def show_graph(self):
        for node, neighbors in self.graph.items():
            print(f"{node} -> {', '.join(neighbors)}")

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' -> ')
        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex, end=' -> ')
                visited.add(vertex)
                temp = [n for n in self.graph.get(vertex, []) if n not in visited]
                queue.extend(temp)


if __name__ == "__main__":

    g = Graph()

    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "E")
    g.add_edge("D", "E")

    g.show_graph()

    print("\nBFS Traversal: ")
    g.bfs("A")

    print("\nDFS Traversal: ")
    g.dfs("A")