def linear_search(data, target):
    for i, item in enumerate(data):
        if item == target:
            return i
    return -1

numbers = [10, 30, 50, 70, 90]
print(linear_search(numbers, 70))