# Greedy Algorithms Tutorial

## 🧠 Introduction
Greedy algorithms are a class of algorithms that make the **locally optimal choice** at each step, hoping that these local choices will lead to a globally optimal solution.

> At every stage, a greedy algorithm picks the **best immediate or local option** without worrying about the future consequences.

---

## 🔑 Key Idea
A greedy algorithm follows these steps:
1. **Initialization** – Start with an empty solution set.
2. **Selection** – Choose the best possible option at the current step (based on a certain criterion).
3. **Feasibility check** – Ensure the current choice doesn’t violate constraints.
4. **Repeat** until you reach the desired result.

Greedy algorithms **don’t always give an optimal solution** for every problem, but for certain problems, they’re **both optimal and efficient**.

---

## ✅ Characteristics of Greedy Algorithms
- Make decisions step by step.
- Each decision is **locally optimal**.
- No backtracking.
- Usually efficient (O(n log n) or better).
- Work well for problems with the **“greedy-choice property”** and **“optimal substructure”**.

---

## ⚙️ Example 1: Coin Change Problem (Real-Time: Currency Dispensing Machine)

**Problem:**  
You need to return change using the **least number of coins**.  
Denominations available: ₹10, ₹5, ₹2, ₹1.

**Goal:** Return ₹28 using the minimum number of coins.

**Greedy approach:**  
Always pick the **largest denomination** that’s ≤ remaining amount.

**Step-by-step:**
```
28 → use 10 → remaining 18
18 → use 10 → remaining 8
8 → use 5 → remaining 3
3 → use 2 → remaining 1
1 → use 1 → remaining 0
```
✅ Coins used: 10, 10, 5, 2, 1 → **5 coins total**

**Python Example:**
```python
def min_coins(amount, coins=[10, 5, 2, 1]):
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result

print(min_coins(28))
# Output: [10, 10, 5, 2, 1]
```

**Real-time use:**  
ATM machines and vending machines use this kind of greedy logic to **dispense the fewest number of coins or notes**.

---

## ⚙️ Example 2: Activity Selection Problem (Real-Time: Scheduling)

**Problem:**  
You’re given start and end times of several activities.  
You can perform only one activity at a time.  
Find the **maximum number of activities** that can be done.

| Activity | Start | End |
|-----------|--------|-----|
| A1        | 1      | 3   |
| A2        | 2      | 5   |
| A3        | 4      | 6   |
| A4        | 6      | 7   |
| A5        | 5      | 9   |
| A6        | 8      | 9   |

**Greedy strategy:**  
- Always pick the **activity that ends earliest** (minimizes occupied time).

**Step-by-step:**
1. Sort by end time: A1, A3, A4, A6, A2, A5  
2. Pick A1 (ends at 3)  
3. Next activity that starts ≥ 3 → A3 (starts at 4)  
4. Next that starts ≥ 6 → A4 (starts at 6)  
5. Next that starts ≥ 7 → A6 (starts at 8)  

✅ Maximum activities = 4 → **A1, A3, A4, A6**

**Python Example:**
```python
def activity_selection(activities):
    activities.sort(key=lambda x: x[1])  # sort by end time
    selected = [activities[0]]
    last_end = activities[0][1]

    for start, end in activities[1:]:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected

activities = [(1,3), (2,5), (4,6), (6,7), (5,9), (8,9)]
print(activity_selection(activities))
# Output: [(1, 3), (4, 6), (6, 7), (8, 9)]
```

**Real-time use:**  
Used in:
- **Meeting room scheduling**
- **CPU task scheduling**
- **Job scheduling in operating systems**

---

## 💡 Other Classic Greedy Algorithm Applications

| Problem | Real-Life Analogy |
|----------|------------------|
| **Kruskal’s / Prim’s Algorithm** | Designing minimum cost road or network connections (telecom, power grid) |
| **Huffman Coding** | Data compression (used in ZIP files, JPEGs, etc.) |
| **Dijkstra’s Algorithm** | GPS route optimization |
| **Fractional Knapsack** | Resource allocation (e.g., maximizing profit under weight/cost constraints) |

---

## 🧩 Summary

| Feature | Greedy Algorithm |
|----------|------------------|
| Decision Strategy | Local optimum at each step |
| Backtracking | No |
| Efficiency | Usually high |
| Best Suited For | Problems with greedy-choice and optimal substructure properties |
| Common Examples | Coin change, activity selection, Kruskal’s MST, Huffman coding |

---

## 📘 Conclusion
Greedy algorithms are an elegant and efficient strategy for solving optimization problems. They’re particularly useful in **resource allocation, scheduling, and routing problems**.

