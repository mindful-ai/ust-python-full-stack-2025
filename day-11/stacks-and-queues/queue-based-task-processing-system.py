''' 
Problem Description
--------------------------------------------------------------------------------------------

Implement a Task Queue Manager using a queue data structure that:

    Accepts tasks with metadata (task ID, description, priority, processing time).
    Processes them in order of arrival (FIFO).

    Allows:

        - Pausing task execution.
        - Resuming from where it stopped.
        - Cancelling specific tasks by ID.
        - Viewing pending tasks.

Menu:

    1. Add Task
    2. Process Tasks
    3. Pause
    4. Resume
    5. Cancel Task
    6. Show Pending Tasks
    7. Exit


'''
from stack import Stack
from queue import Queue

from collections import deque

import time



# ---------- To-Do Task Manager ----------

# ✅ ⚠️ ↩️ 🔁 📝 👋 📭

class TodoApp:

    def __init__(self):
        self.tasks = Queue()
        self.undo_stack = Stack()
        self.redo_stack = Stack()

    def add_task(self, task):
        # TODO: Enqueue task, log action in undo stack, clear redo stack
        self.tasks.enqueue(task)
        self.undo_stack.push(("add", task))
        self.redo_stack.clear()
        print(f"✅  Task added: {task}")


    def complete_task(self):
        # TODO: Dequeue a task (if available) and log completion
        task = self.tasks.dequeue()
        if task:
            self.undo_stack.push(("complete", task))
            self.redo_stack.clear()
            print(f"✅  Task completed: {task}")
        else:
            print("⚠️  No tasks to complete")

    def undo(self):
        # TODO: Undo the most recent action
        # Hint: Pop from undo stack and reverse the operation
        if self.undo_stack.is_empty():
            print("⚠️  Nothing to undo")
            return
        
        action, task = self.undo_stack.pop()
        if action == "add":
            self._remove_task(task)
            print(f"↩️  Undid the addtion of: {task}")
        elif action == 'complete':
            self.tasks.queue.appendleft(task)
            print(f"↩️  Undid the completion of: {task}")

        self.redo_stack.push((action, task))

    def redo(self):
        # TODO: Redo an undone action
        if self.redo_stack.is_empty():
            print("⚠️  Nothing to redo")
            return
        
        action, task = self.redo_stack.pop()
        if action == "complete":
            self._remove_task(task)
            print(f"🔁  Redid the completion of: {task}")
        elif action == 'add':
            self.tasks.enqueue(task)
            print(f"🔁  Redid the addition of: {task}")
            
        self.undo_stack.push((action, task))

    def _remove_task(self, task):
        # TODO: Helper function to remove a task by name from queue
        temp = deque()
        found = False
        while not self.tasks.is_empty():
            t = self.tasks.dequeue()
            if t == task and not found:
                found = True
                continue
            temp.append(t)
        self.tasks.queue = temp

    def show_tasks(self):
        # TODO: Display all pending tasks nicely
        if len(self.tasks) == 0:
            print("\n⚠️  No tasks pending")
        else:
            print("\n📝  Pending tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")
            print()

if __name__ == "__main__":

    app = TodoApp()
    while True:
        print("\n=== TO-DO MANAGER ===")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Undo")
        print("4. Redo")
        print("5. Show Tasks")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            task = input("Enter task description: ")
            app.add_task(task)
        elif choice == "2":
            app.complete_task()
        elif choice == "3":
            app.undo()
        elif choice == "4":
            app.redo()
        elif choice == "5":
            app.show_tasks()
        elif choice == "6":
            print("👋 Exiting To-Do Manager. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice!")
        
        time.sleep(0.5)    