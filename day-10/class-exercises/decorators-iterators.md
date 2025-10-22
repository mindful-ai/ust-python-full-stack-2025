# 🧠 Python Assessment Problems

## Problem 1: Using Built-in Decorators

### 🎯 Objective
Demonstrate the use of built-in decorators such as `@classmethod`, `@staticmethod`, and `@property` in Python.

### 📝 Problem Statement
Create a class **`BookStore`** that manages books in a store.  
Each book has attributes like `title`, `author`, and `price`.

Implement the following:
1. A **class variable** `discount_rate` that applies a discount to all books.
2. A **classmethod** `set_discount(cls, rate)` that sets the global discount rate for all books.
3. A **staticmethod** `is_valid_price(price)` that returns `True` if the price is positive.
4. A **property** `final_price` that returns the discounted price of the book.
5. A **setter** for `price` that ensures price cannot be negative. (@price.setter)
6. A **deleter** for `price` that sets it to `None` and prints `"Price deleted."`. ( @price.deleter)

#### Example
```python
b1 = BookStore("Python 101", "John Doe", 500)
BookStore.set_discount(0.1)
print(b1.final_price)   # 450.0

b1.price = 600
del b1.price
```
---

## Problem 2: Creating an Iterator for Fibonacci Series

### 🎯 Objective
Demonstrate understanding of **iterators** and the `__iter__()` and `__next__()` methods in Python.

### 📝 Problem Statement
Create a class **`Fibonacci`** that implements an iterator to generate Fibonacci numbers up to a given limit.

Implement the following:
1. `__init__(self, limit)` → initializes the Fibonacci iterator.
2. `__iter__(self)` → returns the iterator object itself.
3. `__next__(self)` → returns the next Fibonacci number until the limit is reached, then raises `StopIteration`.

#### Example
```python
fib = Fibonacci(50)
for num in fib:
    print(num, end=" ")
```
**Output:**
```
0 1 1 2 3 5 8 13 21 34
```

### 💡 Hint
- Keep track of two previous numbers (`a` and `b`) in each iteration.
- Raise `StopIteration` when the next number exceeds the limit.
