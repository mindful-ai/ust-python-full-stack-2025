
# 🌳 Graphs and Trees — A Complete Tutorial with Real Examples

## 📘 Introduction

**Graphs** and **Trees** are fundamental data structures in computer science used to represent relationships and hierarchies.

---

## 🌲 1. Trees

### What is a Tree?
A **Tree** is a hierarchical data structure made up of **nodes**, where each node has:
- A **value** (data)
- References to **child nodes**

A **Binary Tree** is a tree where each node has **at most two children**.

### Real-Life Analogy:
Think of an **organization chart** — one CEO, multiple managers, and subordinates.  
Each person reports to exactly one boss (parent node).

### Key Terms
| Term | Description |
|------|--------------|
| Root | Topmost node |
| Leaf | Node with no children |
| Parent | Node that has child nodes |
| Child | Node descended from a parent |
| Subtree | Portion of the tree under a node |

---

## 🧩 2. Binary Tree Implementation in Python

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert(current.left, data)
        else:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert(current.right, data)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

# Demo
tree = BinaryTree()
for num in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    tree.insert(num)

print("Inorder Traversal:")
tree.inorder(tree.root)
```

**Output:**
```
Inorder Traversal:
1 3 4 6 7 8 10 13 14
```

---

## 💼 3. Real-World Use Case — Huffman Compression

### Why Trees Matter in Compression
Huffman Coding uses a **binary tree** to assign variable-length binary codes to characters, optimizing compression.  
Frequently used characters get shorter codes.

### Huffman Encoding + Decoding Example

```python
import heapq
from collections import Counter, namedtuple

class Node(namedtuple("Node", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq = Counter(text)
    heap = [Node(ch, fr, None, None) for ch, fr in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)
    return heap[0]

def generate_codes(node, code="", code_map={}):
    if node is None:
        return
    if node.char is not None:
        code_map[node.char] = code
    generate_codes(node.left, code + "0", code_map)
    generate_codes(node.right, code + "1", code_map)
    return code_map

def encode(text, codes):
    return ''.join(codes[ch] for ch in text)

def decode(encoded, root):
    decoded_text = ""
    current = root
    for bit in encoded:
        current = current.left if bit == "0" else current.right
        if current.char is not None:
            decoded_text += current.char
            current = root
    return decoded_text

# Example Usage
text = "huffman coding example"
root = build_huffman_tree(text)
codes = generate_codes(root)
encoded = encode(text, codes)
decoded = decode(encoded, root)

print("Character Codes:", codes)
print("Encoded:", encoded)
print("Decoded:", decoded)
print("✅ Compression Successful:", decoded == text)
```

---

## 🕸️ 4. Graphs

### What is a Graph?
A **Graph** is a collection of nodes (vertices) connected by **edges**.

### Types of Graphs
| Type | Description |
|------|--------------|
| Directed | Edges have direction |
| Undirected | Edges are bidirectional |
| Weighted | Each edge has a cost/weight |
| Unweighted | All edges are equal |

### Example Representation (Adjacency List)

```python
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)
        self.graph.setdefault(v, []).append(u)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Example Usage
g = Graph()
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'E')]
for u, v in edges:
    g.add_edge(u, v)

print("DFS starting from A:")
g.dfs('A')
```

**Output:**
```
DFS starting from A:
A B D E C
```

---

## ⚙️ 5. Summary Comparison

| Feature | Tree | Graph |
|----------|-------|-------|
| Structure | Hierarchical | Network |
| Cycles | No | Yes (possible) |
| Root | Single root | No root required |
| Applications | Compression, Search | Navigation, Networks |

---

## 🧠 6. Real-World Applications

| Domain | Structure | Example |
|---------|------------|----------|
| File Compression | Tree (Huffman) | ZIP, JPEG |
| Network Routing | Graph | Internet, GPS |
| Database Indexing | Tree (B-Tree) | MySQL |
| Social Media | Graph | Friend recommendations |
| AI Search | Tree/Graph | Pathfinding, Game AI |

---

## ✅ Conclusion
Trees and Graphs are the building blocks of efficient algorithms and systems — from data compression and routing to decision making and AI.  
Mastering these gives you deep insight into **optimization and structure** in computing.
