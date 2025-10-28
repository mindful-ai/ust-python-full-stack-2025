# 🧩 Dynamic Programming (DP) Tutorial

## 🧠 What is Dynamic Programming?
**Dynamic Programming** is a method to solve complex problems by breaking them into **smaller overlapping subproblems**, solving each once, and **storing their results** to avoid redundant computations.

> “If you find yourself solving the same subproblem multiple times — store the answer and reuse it.”

---

## 🚴 Analogy
Imagine climbing stairs.  
You can take **1 or 2 steps** at a time.  
How many ways can you reach the top of `n` stairs?

If `n = 3`:
- Step combinations:  
  (1,1,1), (1,2), (2,1) → **3 ways**

You notice:
```
ways(3) = ways(2) + ways(1)
```
That’s the **DP principle** — the solution for `n` depends on smaller `n`.

---

## ✳️ Step-by-Step Example — Fibonacci Numbers

### Problem:
Compute the `n`th Fibonacci number.

**Recursive Definition:**
```
F(n) = F(n-1) + F(n-2)
F(0) = 0, F(1) = 1
```

### 🐢 Naive Recursion:
```python
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)
```
This works, but it’s **very slow** (O(2ⁿ)) because it repeats subproblems.

---

### 🚀 Dynamic Programming Solution (Memoization)
```python
def fib_dp(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_dp(n-1, memo) + fib_dp(n-2, memo)
    return memo[n]

print(fib_dp(10))  # Output: 55
```
✅ **Improved Efficiency:** O(n)

---

### 💾 Bottom-Up (Tabulation) Approach
```python
def fib_tab(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

print(fib_tab(10))  # Output: 55
```

---

## 🧰 Real-Time Use Case — Minimum Cost Path (Grid Traversal)

### 🏙️ Problem:
A robot moves in a grid (m x n) starting at the top-left (0,0) and wants to reach the bottom-right (m-1,n-1).  
Each cell `(i,j)` has a cost, and the robot can move **only right or down**.  
Find the **minimum total cost path**.

### Example Grid:
|   |   |   |
|---|---|---|
| 1 | 3 | 1 |
| 1 | 5 | 1 |
| 4 | 2 | 1 |

The **optimal path** is 1 → 3 → 1 → 1 → 1 = **7**

---

### 🧮 DP Solution:
```python
def min_cost_path(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[0]*cols for _ in range(rows)]
    
    dp[0][0] = grid[0][0]

    # Fill first row
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Fill first column
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Fill remaining cells
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]

# Example usage
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print("Minimum Cost Path:", min_cost_path(grid))
```

✅ Output:
```
Minimum Cost Path: 7
```

---

### 🔍 Real-World Analogy:
This type of DP is used in:
- **Navigation systems** (finding least-cost route through a weighted map)
- **Network routing** (finding shortest or cheapest path)
- **Robotics** (path planning with energy cost minimization)
- **Supply chain optimization** (min-cost logistics)

---

## 🧭 Summary

| Concept | Description |
|----------|--------------|
| **Overlapping subproblems** | Same smaller problems occur many times |
| **Optimal substructure** | Overall solution can be built from subproblems |
| **Memoization** | Top-down recursion + caching |
| **Tabulation** | Bottom-up iteration |
