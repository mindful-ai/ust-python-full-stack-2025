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