# Reduces memory usage by sharing common data between multiple similar objects.

'''

We’re simulating a forest that has 1,000,000 trees.

Each tree has:
    x, y coordinates (unique for every tree)
    type (shared data like color, texture, etc.)

Without Flyweight — each tree stores its own TreeType data.
With Flyweight — trees share common TreeType objects.


'''

import random
import psutil
import os
import gc

# -----------------------------
# Utility function to measure memory
# -----------------------------
def memory_usage_mb():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)  # in MB

# -----------------------------
# Version 1: Without Flyweight
# -----------------------------
class Tree:
    def __init__(self, x, y, name, color, texture):
        self.x = x
        self.y = y
        self.name = name
        self.color = color
        self.texture = texture

class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, name, color, texture):
        self.trees.append(Tree(x, y, name, color, texture))

def create_forest(n=200_000):
    forest = Forest()
    tree_types = [("Oak", "Green", "Rough"), ("Pine", "DarkGreen", "Smooth"), ("Birch", "LightGreen", "Flaky")]
    for _ in range(n):
        name, color, texture = random.choice(tree_types)
        forest.plant_tree(random.randint(0, 1000), random.randint(0, 1000), name, color, texture)
    return forest

# -----------------------------
# Version 2: With Flyweight
# -----------------------------
class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

class TreeFactory:
    _tree_types = {}

    @staticmethod
    def get_tree_type(name, color, texture):
        key = (name, color, texture)
        if key not in TreeFactory._tree_types:
            TreeFactory._tree_types[key] = TreeType(name, color, texture)
        return TreeFactory._tree_types[key]

class TreeFlyweight:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

class ForestFlyweight:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, name, color, texture):
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        self.trees.append(TreeFlyweight(x, y, tree_type))

def run_with_flyweight(n=200_000):
    forest = ForestFlyweight()
    tree_types = [("Oak", "Green", "Rough"), ("Pine", "DarkGreen", "Smooth"), ("Birch", "LightGreen", "Flaky")]
    for _ in range(n):
        name, color, texture = random.choice(tree_types)
        forest.plant_tree(random.randint(0, 1000), random.randint(0, 1000), name, color, texture)
    return forest

# -----------------------------
# Benchmark comparison
# -----------------------------
if __name__ == "__main__":
    print("🌲 Flyweight Pattern Memory Comparison\n")

    n = 200_000  # number of trees

    print(f"Creating {n} trees WITHOUT Flyweight...")
    mem_before = memory_usage_mb()
    forest1 = create_forest(n)
    mem_after = memory_usage_mb()
    print(f"Memory Used (No Flyweight): {mem_after - mem_before:.2f} MB\n")

    # Cleanup
    del forest1
    gc.collect()

    print(f"Creating {n} trees WITH Flyweight...")
    mem_before = memory_usage_mb()
    forest2 = run_with_flyweight(n)
    mem_after = memory_usage_mb()
    print(f"Memory Used (With Flyweight): {mem_after - mem_before:.2f} MB\n")

    print(f"Unique tree types created: {len(TreeFactory._tree_types)}")
