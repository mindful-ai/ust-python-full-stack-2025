from collections import deque
import time

class Queue:

    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        raise IndexError("Dequeue from empty queue")
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def clear(self):
        self.queue.clear()

    def __len__(self):
        return len(self.queue)
    
    def __iter__(self):
        return iter(self.queue)
    
    def __repr__(self):
        return f"Queue({list(self.queue)})"

if __name__ == "__main__":

    # Task scheduling 

    tasks = Queue()

    tasks.enqueue("Send email")
    tasks.enqueue("Generate report")
    tasks.enqueue("Upload backup")

    while not tasks.is_empty():

        current_task = tasks.dequeue()
        print(f"Processing: {current_task}")
        time.sleep(1)