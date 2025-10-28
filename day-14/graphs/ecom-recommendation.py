from collections import defaultdict, deque

class ProductGraph:
    
    def __init__(self):
        self.graph = defaultdict(set)

    def add_edge(self, product1, product2):
        """Add bidirectional relationship (products bought together)."""
        self.graph[product1].add(product2)
        self.graph[product2].add(product1)

    def recommend(self, product, level=1):
        """
        Recommend products related within N-level connections.
        level=1 -> directly related
        level=2 -> includes 'friends of friends' products
        """
        visited = set([product])
        queue = deque([(product, 0)])
        recommendations = set()

        while queue:
            current, depth = queue.popleft()
            if depth < level:
                for neighbor in self.graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        recommendations.add(neighbor)
                        queue.append((neighbor, depth + 1))
        return recommendations


# ------------------ DEMO ------------------ #
pg = ProductGraph()

# Simulate co-purchase relationships
relations = [
    ("Phone", "Case"),
    ("Phone", "Charger"),
    ("Phone", "Screen Protector"),
    ("Charger", "Cable"),
    ("Laptop", "Mouse"),
    ("Laptop", "Keyboard"),
    ("Mouse", "Mouse Pad"),
]

for p1, p2 in relations:
    pg.add_edge(p1, p2)

# Recommend products for a user viewing a "Phone"
print("Directly related to Phone (Level 1):", pg.recommend("Phone", level=1))
print("Related up to 2 levels (Level 2):", pg.recommend("Phone", level=2))
