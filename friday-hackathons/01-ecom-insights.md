# 🧠 Hackathon Problem: “E-Commerce Insights — Customer Purchase Analytics”

## Problem Description

You are given a list of **purchase records** from an online shopping platform.  
Each purchase record is represented as a **tuple** in the format:

```python
(customer_name, item, price, quantity, payment_mode)
```

### Example Dataset

```python
transactions = [
    ("Alice", "Book", 250, 2, "Credit"),
    ("Bob", "Laptop", 55000, 1, "UPI"),
    ("Alice", "Pen", 20, 10, "Cash"),
    ("Bob", "Mouse", 800, 1, "Credit"),
    ("Charlie", "Keyboard", 1500, 1, "UPI"),
    ("Alice", "Notebook", 80, 3, "Credit"),
    ("Bob", "Monitor", 12000, 1, "UPI"),
    ("Charlie", "USB Cable", 300, 2, "Cash"),
    ("Daisy", "Laptop Bag", 1200, 1, "Credit"),
    ("Alice", "Lamp", 600, 1, "UPI")
]
```

---

## Your Tasks

Using **loops, conditionals, and Python data structures**, perform an analysis and output a **summary dictionary** with the following information:

1. **Total unique customers** → Count of distinct customer names.  
2. **Total revenue** → Sum of (`price × quantity`) for all transactions.  
3. **Customer total spending** → Dictionary where keys are customer names and values are total amounts spent.  
4. **Top spender** → Customer who spent the most.  
5. **Most popular payment mode** → The payment method used most frequently.  
6. **Average spend per transaction** → Average of all transaction totals.  
7. **Customers who used more than one payment mode** → List of such customer names.  
8. **Categorize customers** into:
   - `'High Value'` → Total spend > ₹10,000  
   - `'Medium Value'` → ₹1,000 ≤ spend ≤ ₹10,000  
   - `'Low Value'` → spend < ₹1,000  

The final output should be a **dictionary** with all these summaries.

---

## Expected Output (Example)

```python
{
  'total_customers': 4,
  'total_revenue': 72370,
  'customer_spending': {
      'Alice': 2030,
      'Bob': 67800,
      'Charlie': 2100,
      'Daisy': 1200
  },
  'top_spender': 'Bob',
  'most_common_payment_mode': 'UPI',
  'average_transaction_value': 7237.0,
  'multi_payment_customers': ['Alice', 'Charlie'],
  'customer_segments': {
      'High Value': ['Bob'],
      'Medium Value': ['Charlie', 'Daisy'],
      'Low Value': ['Alice']
  }
}
```

---

## Core Python Concepts Covered

✅ Lists & Tuples  
✅ Dictionaries & nested structures  
✅ Loops & conditional branching  
✅ Built-in functions (`sum`, `len`, `set`, `max`, etc.)  
✅ Basic aggregation logic  

---

## Hints (Libraries to Explore)

| Library | What It Can Help With |
|----------|----------------------|
| `collections` | Use `Counter` to find most common payment mode. |
| `statistics` | Use `mean()` for average transaction value. |
| `operator` | Use `itemgetter()` to identify top spender easily. |
| `itertools` | Use `groupby()` if you wish to group transactions by customer. |
| `pprint` | Use `pprint` to print nested dicts neatly. |

*(Encourage participants to solve mostly with pure Python first, and then optionally use one or more of these libraries to simplify code.)*

---

## Evaluation Criteria

| Criterion | Description |
|------------|-------------|
| ✅ Correctness | All required outputs computed accurately |
| ⚙️ Logic & Control Flow | Efficient and readable loop & conditional logic |
| 🧩 Data Structures | Proper use of lists, tuples, dicts |
| 🧰 Built-in Functions | Effective use of standard Python tools |
| ✨ Code Quality | Clear, formatted, and commented |
| 🚀 Bonus | Optional library usage, modular code (functions) |

---

## Suggested Timeline (for a 2-hour hackathon)

| Time | Task |
|------|------|
| 0–20 min | Understand problem and plan approach |
| 20–70 min | Write code using loops and conditions |
| 70–90 min | Integrate summaries and testing |
| 90–120 min | Optional library enhancements & final presentation |
