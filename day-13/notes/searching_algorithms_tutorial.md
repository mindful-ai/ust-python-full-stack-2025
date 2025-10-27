# 🔍 Searching Algorithms in Python — Workshop Tutorial

## 🧠 Why Learn Searching Algorithms?

Even though Python provides built-in search functions like `in`, `index()`, and list comprehensions, understanding **search algorithms** like **Linear Search** and **Binary Search** is crucial because:

1. **Control and Customization:** You can adapt them to work on complex data structures (e.g., dictionaries, objects, or custom classes).
2. **Optimization Insight:** Helps you analyze performance and know when to prefer one algorithm over another.
3. **Foundation for Advanced Topics:** Binary search logic appears in machine learning model tuning, database indexing, and divide-and-conquer algorithms.

---

## 🧩 Linear Search

### Concept
Linear search sequentially scans every element in a collection until the target is found or the list ends.

### Time Complexity
- **Best case:** O(1)
- **Worst case:** O(n)

### Example
```python
def linear_search(data, target):
    for i, item in enumerate(data):
        if item == target:
            return i
    return -1

numbers = [10, 30, 50, 70, 90]
print(linear_search(numbers, 70))  # Output: 3
```

---

## ⚙️ Binary Search

### Concept
Binary search works only on **sorted data**. It repeatedly divides the search space in half until the element is found.

### Time Complexity
- **Best case:** O(1)
- **Worst case:** O(log n)

### Example
```python
def binary_search(data, target):
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

numbers = [10, 20, 30, 40, 50, 60, 70]
print(binary_search(numbers, 40))  # Output: 3
```

---

## 🎯 Why Not Just Use Python’s Built-in Search?

Let’s compare both methods.

```python
import time

data = list(range(1, 10_000_000))

# Built-in 'in' operator
start = time.time()
found = 9_999_999 in data
print("Built-in search time:", time.time() - start)

# Manual Binary Search
def binary_search(data, target):
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

start = time.time()
found = binary_search(data, 9_999_999)
print("Binary search time:", time.time() - start)
```

✅ You’ll notice **binary search** is faster than linear search for large sorted datasets and often comparable to or better than built-ins when you need **customization**.

---

## 🧩 Real-World Assessment Problems

### 1️⃣ Linear Search — Hospital Patient Lookup

#### Problem
You are developing a **Hospital Management System**. Nurses need to find a patient by name in an **unsorted** list.

#### Task
Implement a function to perform a **Linear Search**.

#### Function Signature
```python
def find_patient(patients, name):
    pass
```

#### Input Example
```python
patients = [
    {"name": "Anita Sharma", "age": 30, "disease": "Fever"},
    {"name": "Ravi Kumar", "age": 42, "disease": "Diabetes"},
    {"name": "John Doe", "age": 45, "disease": "Hypertension"}
]
```

#### Expected Output
```
Patient Found: {'name': 'John Doe', 'age': 45, 'disease': 'Hypertension'}
```

#### Hint
- Compare names case-insensitively (`lower()`).
- The list is **unsorted**, so use linear search.

---

### 2️⃣ Binary Search — Patient Age Finder

#### Problem
You have a **sorted list of patients by age**. You must check if a patient of a specific age exists.

#### Task
Implement a **Binary Search** to find if a patient’s age exists.

#### Function Signature
```python
def find_patient_by_age(sorted_patients, target_age):
    pass
```

#### Input Example
```python
patients = [
    {"name": "Aarav Sharma", "age": 22, "disease": "Cold"},
    {"name": "Diya Iyer", "age": 36, "disease": "Fever"},
    {"name": "Rohan Gupta", "age": 47, "disease": "Asthma"}
]
```

#### Expected Output
```
Patient with age 36 found.
```

#### Hint
- Use the `age` field for comparison.
- Ensure the patient list is sorted by age.

---

## 🧾 Data for Practice

A sample dataset `patients.csv` with 100 fake patient records is provided for exercises.

Each record has:
```
name, age, disease
```

You can load it using:
```python
import pandas as pd
patients = pd.read_csv("patients.csv")
print(patients.head())
```

---

## 💡 Instructor Notes

| Criterion | Weight |
|------------|---------|
| Correct search logic | 40% |
| Edge case handling | 20% |
| Code readability | 20% |
| Understanding of algorithm choice | 20% |

---

## ✅ Summary

| Algorithm | Use Case | Works On | Time Complexity |
|------------|-----------|-----------|----------------|
| Linear Search | Unsorted data (e.g., new patient arrivals) | Any list | O(n) |
| Binary Search | Sorted data (e.g., age, ID, price) | Sorted list | O(log n) |

---
