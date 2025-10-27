# 🧠 Sorting Algorithms Workshop Tutorial (with Real-World Examples)

## 🎯 Objective
This tutorial aims to provide a hands-on understanding of **sorting algorithms**, their working principles, and their **importance in real-world applications**, even when Python provides built-in sorting functions.

---

## 📘 Why Learn Sorting Algorithms?
You might wonder — why study sorting algorithms when we can just do:
```python
data.sort()
# or
sorted(data)
```
That’s a fair question! But here’s why you **must** learn sorting algorithms:

1. **Interviews and Competitive Programming** – They test your ability to think algorithmically.
2. **Optimization in Large Systems** – Built-in sorts are general-purpose. Custom algorithms may perform better for domain-specific data.
3. **Control and Customization** – You can modify sorting logic for multi-level or conditional sorting (e.g., by category, then by price).
4. **Understanding System Internals** – Python’s `sorted()` uses **Timsort**, a hybrid algorithm based on merge and insertion sort.
5. **When Built-in Sorts Fail** – If you are sorting **streaming data**, **custom objects**, or data in **external memory**, you’ll need your own sorting logic.

---

## 🧩 Basic Sorting Algorithms

### 1️⃣ Bubble Sort
**Idea**: Repeatedly swap adjacent elements if they are in the wrong order.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

data = [64, 25, 12, 22, 11]
print("Bubble Sorted:", bubble_sort(data))
```

**Time Complexity:** O(n²)  
**Best Use Case:** Small datasets or nearly sorted lists.

---

### 2️⃣ Selection Sort
**Idea**: Repeatedly find the minimum element and place it at the beginning.

```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

data = [29, 10, 14, 37, 13]
print("Selection Sorted:", selection_sort(data))
```

**Time Complexity:** O(n²)  
**Best Use Case:** When memory writes are expensive.

---

### 3️⃣ Insertion Sort
**Idea**: Builds a sorted array one element at a time.

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

data = [12, 11, 13, 5, 6]
print("Insertion Sorted:", insertion_sort(data))
```

**Time Complexity:** O(n²)  
**Best Use Case:** Nearly sorted or small datasets.

---

### 4️⃣ Merge Sort
**Idea**: Divide and conquer — divide the list into halves, sort them, and merge.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

data = [38, 27, 43, 3, 9, 82, 10]
print("Merge Sorted:", merge_sort(data))
```

**Time Complexity:** O(n log n)  
**Best Use Case:** Large datasets or linked lists.

---

### 5️⃣ Quick Sort
**Idea**: Pick a pivot, partition the array, and recursively sort subarrays.

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

data = [10, 7, 8, 9, 1, 5]
print("Quick Sorted:", quick_sort(data))
```

**Time Complexity:** O(n log n) average, O(n²) worst  
**Best Use Case:** General-purpose fast sorting.

---

## 🏢 Real-World Example — E-commerce Product Sorting

Let’s say we have product data:
```python
products = [
    {"name": "Laptop", "price": 75000, "rating": 4.6},
    {"name": "Headphones", "price": 1500, "rating": 4.3},
    {"name": "Smartphone", "price": 25000, "rating": 4.5},
    {"name": "Monitor", "price": 12000, "rating": 4.2}
]
```

### Sort by Price (ascending)
```python
sorted_by_price = sorted(products, key=lambda x: x["price"])
print(sorted_by_price)
```

### Sort by Rating (descending)
```python
sorted_by_rating = sorted(products, key=lambda x: x["rating"], reverse=True)
print(sorted_by_rating)
```

✅ **Why Not Use Built-ins Always?**
Imagine your products are **streaming live from multiple sources** — you can’t load all data into memory to use `sorted()`.  
Instead, you can implement a **custom merge sort** that works on chunks of data stored on disk.

---

## 🧠 Assessment Problem: Sorting E-commerce Data

### 📝 Problem Statement
You are working for an e-commerce platform like **ShopSmart**.  
The company wants to sort product data in different ways for analytics.

### Your Tasks
1. Read the dataset (`ecommerce_data.csv`) that contains:
   ```csv
   product_id,product_name,category,price,rating,sales_count
   ```
2. Implement the following:
   - Sort by **price** (ascending)
   - Sort by **rating** (descending)
   - Sort by **sales_count** (descending)
3. Implement **merge sort** manually for at least one of the sortings.
4. Compare your algorithm’s performance with Python’s built-in `sorted()` using the `time` module.
5. Write observations and conclusion.

### 💡 Bonus Challenge
Implement a **multi-level sort**:  
- Sort by category, then by rating (descending), then by price (ascending).

---

## ✅ Expected Learning Outcomes
By the end of this session, you will be able to:
- Understand how different sorting algorithms work.
- Know their performance trade-offs.
- Apply sorting logic to real-world data scenarios.
- Appreciate why built-in sorts aren’t always enough.

---

**Author:** Purushotham S  
**Topic:** Sorting Algorithms Workshop  
**Language:** Python  
