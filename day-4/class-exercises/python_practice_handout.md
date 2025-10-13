# 🐍 Python Practice Handout

This handout contains problem statements for practicing key Python concepts:
- Comprehensions  
- Lambda / Map / Filter / Zip  
- Built-in Modules  

Each problem specifies the **input** and the **expected output**.  
Write your own solutions before checking the answers separately.

---

## 🧩 SECTION 1 — PYTHON COMPREHENSIONS

### 1️⃣ Square of Even Numbers
**Problem:**  
Given a list of integers, create a new list that contains the square of even numbers only.  

**Input:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
**Expected Output:**
```
[4, 16, 36, 64, 100]
```

---

### 2️⃣ Extract Vowels from a String
**Problem:**  
Given a string, extract all vowels (a, e, i, o, u) and store them in a list.  


**Input:**
```python
text = "Python comprehensions are powerful!"
```
**Expected Output:**
```
['o', 'o', 'e', 'e', 'i', 'o', 'a', 'e', 'o', 'e', 'u']
```

---

### 3️⃣ Price Dictionary with Discounts
**Problem:**  
Given a dictionary of item prices, create a new dictionary with a 10% discount applied to items priced above 200.  

**Input:**
```python
prices = {'pen': 50, 'book': 300, 'bag': 700, 'pencil': 30}
```
**Expected Output:**
```
{'pen': 50, 'book': 270.0, 'bag': 630.0, 'pencil': 30}
```

---

### 4️⃣ Matrix Transpose
**Problem:**  
Given a 3x3 matrix (list of lists), transpose it using a comprehension.  

**Input:**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
**Expected Output:**
```
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

---

### 5️⃣ Unique Words and Their Lengths
**Problem:**  
Given a paragraph, find all unique words and create a dictionary where each word maps to its length. Ignore punctuation and case.  

**Input:**
```python
text = "Python is powerful, and python is easy to learn!"
```
**Expected Output:**
```
{'python': 6, 'is': 2, 'easy': 4, 'powerful': 8, 'and': 3, 'to': 2, 'learn': 5}

```


### 6 Flatten a list

**Problem:**
Flatten a two dimensional list.

**Input:**
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

**Expected Output:**
```python
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## ⚙️ SECTION 2 — LAMBDA, MAP, FILTER, ZIP

### 1️⃣ Celsius to Fahrenheit Conversion
**Input:**
```python
temps_c = [0, 20, 37, 100]
```
**Expected Output:**
```
[32.0, 68.0, 98.6, 212.0]
```

---

### 2️⃣ Filter High-Value Transactions
**Input:**
```python
transactions = [1200, 8000, 500, 15000, 2300, 7000]
```
**Expected Output:**
```
[8000, 15000, 7000]
```

---

### 3️⃣ Square Only Odd Numbers
**Input:**
```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
**Expected Output:**
```
[1, 9, 25, 49, 81]
```

---

### 4️⃣ Combine Names and Scores
**Input:**
```python
names = ['Asha', 'Vikram', 'Riya']
marks = [85, 92, 78]
```
**Expected Output:**
```
['Name: Asha, Score: 85', 'Name: Vikram, Score: 92', 'Name: Riya, Score: 78']
```

---

### 5️⃣ Product Totals from Multiple Lists
**Input:**
```python
products = ['Pen', 'Book', 'Bag']
prices = [10, 200, 500]
quantities = [5, 2, 1]
```
**Expected Output:**
```
[('Pen', 50), ('Book', 400), ('Bag', 500)]
```

---

## 🧮 SECTION 3 — BUILT-IN MODULES

### 1️⃣ Sort Employees by Salary (`operator`)
**Input:**
```python
employees = [
    {'name': 'Asha', 'salary': 52000},
    {'name': 'Vikram', 'salary': 68000},
    {'name': 'Riya', 'salary': 45000},
]
```
**Expected Output:**
```
[{'name': 'Vikram', 'salary': 68000}, {'name': 'Asha', 'salary': 52000}, {'name': 'Riya', 'salary': 45000}]
```

---

### 2️⃣ Count Words in a Paragraph (`collections.Counter`)
**Input:**
```python
text = "Python is powerful and fast. Python is fun and flexible."
```
**Expected Output:**
```
[('python', 2), ('is', 2), ('and', 2)]
```

---

### 3️⃣ Generate All 2-Item Combinations (`itertools.combinations`)
**Input:**
```python
students = ['Asha', 'Vikram', 'Riya', 'John']
```
**Expected Output:**
```
[('Asha', 'Vikram'), ('Asha', 'Riya'), ('Asha', 'John'), ('Vikram', 'Riya'), ('Vikram', 'John'), ('Riya', 'John')]
```

---

### 4️⃣ Find Product of a List (`functools.reduce` and `operator.mul`)
**Input:**
```python
nums = [2, 3, 4, 5]
```
**Expected Output:**
```
120
```

---

### 5️⃣ Find the Hypotenuse (`math.hypot`)
**Input:**
```python
a, b = 3, 4
```
**Expected Output:**
```
5.0
```

---

### 🌟 Bonus: Group Words by Starting Letter (`collections.defaultdict`)
**Input:**
```python
words = ['apple', 'ant', 'ball', 'bat', 'cat']
```
**Expected Output:**
```
{'a': ['apple', 'ant'], 'b': ['ball', 'bat'], 'c': ['cat']}
```

---

