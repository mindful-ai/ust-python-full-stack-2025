import threading
import time
import random


class CoffeeShop:
    def __init__(self, orders):
        self.orders = orders               # Shared list of coffee orders
        self.lock = threading.Lock()       # Lock to prevent race conditions
        self.completed = {}                # Track how many orders each barista completed

    def prepare_order(self):
        """Each barista thread executes this method."""
        barista_name = threading.current_thread().name
        self.completed[barista_name] = 0   # Initialize barista’s order count

        while True:
            self.lock.acquire()
            if not self.orders:
                self.lock.release()
                break  # No more orders to process

            order = self.orders.pop(0)  # Take an order safely
            self.lock.release()

            print(f"{barista_name} is preparing {order}...")
            time.sleep(random.uniform(1, 3))  # Simulate preparation time
            print(f"{barista_name} finished {order}.")

            self.completed[barista_name] += 1  # Update count

    def start_baristas(self, num_baristas):
        """Create and start multiple barista threads."""
        threads = []
        names = ["Alice", "Bob", "Charlie", "David", "Eve"]

        for i in range(num_baristas):
            t = threading.Thread(target=self.prepare_order, name=names[i])
            threads.append(t)
            t.start()

        for t in threads:
            t.join()  # Wait for all baristas to finish

        print("\nAll orders completed!\n")
        self.print_summary()

    def print_summary(self):
        """Display how many orders each barista completed."""
        print("Summary:")
        for barista, count in self.completed.items():
            print(f"{barista} completed {count} order(s).")


# ✅ Example usage
if __name__ == "__main__":
    orders = ["Latte", "Cappuccino", "Espresso", "Mocha", "Americano", "Macchiato", "Flat White"]
    shop = CoffeeShop(orders)
    shop.start_baristas(3)
