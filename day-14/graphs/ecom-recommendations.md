🛒 Real-Time Example: Product Recommendation using Graphs
### 🎯 Problem Statement

In an e-commerce platform, products are often bought together (e.g., "People who bought Phone also bought Phone Case").
We can model these relationships using a Graph, where:

    - Each node represents a product
    - Each edge represents a co-purchase relationship
    - Once this graph is built, we can:
      - Recommend related items
      - Find top co-occurring products
      - Detect clusters of similar product categories

### 🧠 Conceptual Model

Example product relations:

Phone — Case — Charger — Cable
        \
         — Screen Protector
Laptop — Mouse — Keyboard

###### Goal: When a user views “Phone”, recommend all items connected (directly or indirectly) in the graph.