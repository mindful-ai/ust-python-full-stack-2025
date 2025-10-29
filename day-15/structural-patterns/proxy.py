# Controls access to another object, adding functionality like security, logging, or lazy initialization.
# A credit card acts as a proxy for your bank account — you don’t hand over cash directly.

# Virtual Proxy for a heavy image loader

import time

class RealImage:
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print(f"Loading image {self.filename} from disk...")
        time.sleep(2)
        print("Image loaded.")

    def display(self):
        print(f"Displaying {self.filename}")

class ProxyImage:
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if not self.real_image:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

# Client
if __name__ == "__main__":
    image = ProxyImage("photo.png")
    print("First call:")
    image.display()  # Loads from disk
    print("\nSecond call:")
    image.display()  # Uses cached version
