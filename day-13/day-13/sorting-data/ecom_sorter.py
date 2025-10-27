# ecommerce_sorting.py

orders = [
    # Sample data here
]

# 1. Implement a custom sorting algorithm (e.g., merge sort)
def bubble_sort(data, key_func, reverse=False):
    # Your code here
    pass

# 2. Sorting cases
def sort_by_amount(orders):
    pass

def sort_by_date(orders):
    pass

def sort_by_status(orders):
    pass

# 3. Print Top 5 Orders
def top_five_orders(orders):
    pass

def main():
    print("Case 1: Sorted by total amount (ascending)")
    print(sort_by_amount(orders))

    print("\nCase 2: Sorted by order date (descending)")
    print(sort_by_date(orders))

    print("\nCase 3: Sorted by delivery status (custom order)")
    print(sort_by_status(orders))

    print("\nTop 5 orders by total amount:")
    print(top_five_orders(orders))

if __name__ == "__main__":
    main()
