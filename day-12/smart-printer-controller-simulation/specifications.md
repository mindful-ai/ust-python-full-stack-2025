# 🧩 Smart Print Queue System

### ⏱ Duration: 1 Hour  
### 💡 Difficulty: Intermediate  
### 🧠 Topics: Stacks, Queues, Undo/Redo Operations, OOP in Python  

---

## 🎯 Problem Statement

You are designing a **Smart Print Queue Manager** for an office printer.  
The printer should process documents in **First-In-First-Out (FIFO)** order,  
but also support **Undo** and **Redo** functionalities for user actions.

Your task is to build a **command-line Python program** that uses:
- A **Queue** to manage print jobs in order.
- Two **Stacks** to implement **Undo** and **Redo** operations.

---

## ⚙️ Functional Requirements

### 1️⃣ Add a Print Job  
- User inputs a `document_name`.  
- The job is added to the print queue.  
- Record this action in the Undo stack.  
- Clear the Redo stack.

### 2️⃣ Cancel a Print Job  
- User specifies a `document_name`.  
- If found in the queue, remove it.  
- Record the cancel action in the Undo stack.  
- Clear the Redo stack.

### 3️⃣ Undo Last Action  
- If the last action was `add`, remove that document from the queue.  
- If it was `cancel`, re-add the canceled document.  
- Push the undone action into the Redo stack.

### 4️⃣ Redo Last Undone Action  
- Re-apply the last action undone using the Redo stack.

### 5️⃣ Show Current Queue  
- Display all print jobs currently waiting to be printed (FIFO order).

### 6️⃣ Exit  
- Cleanly terminate the program.

---

## 🧭 Example Interaction

```python
=== SMART PRINT QUEUE ===
1. Add Job
2. Cancel Job
3. Undo
4. Redo
5. Show Queue
6. Exit

> 1
Enter document name: Report.pdf
✅ Added 'Report.pdf' to print queue

> 1
Enter document name: Invoice.pdf
✅ Added 'Invoice.pdf' to print queue

> 5
📄 Print Queue:
1. Report.pdf
2. Invoice.pdf

> 2
Enter document name: Report.pdf
🗑️ Canceled 'Report.pdf'

> 3
↩️ Undo: Re-added 'Report.pdf'

> 5
📄 Print Queue:
1. Report.pdf
2. Invoice.pdf
```

# 🖨️ Smart Print Queue System - Skeleton Code

## Objective
Implement a print queue manager using **Python’s Queue data structure**.  
The system should handle print jobs submitted by multiple users, prioritize urgent documents, and process them efficiently.

---

## 🔧 Skeleton Code

# 🖨️ Smart Print Queue System (with Undo / Redo / Cancel)

## 🎯 Objective
Implement a **menu-driven Smart Print Queue System** using Python, demonstrating the use of **Queues** and **Stacks** together.  
The system manages print jobs, supports cancellation, and allows undo/redo of user actions.

---

## 🔧 Skeleton Code

```python
from queue import Queue

spq = SmartPrintQueue()

def printer(printQueue):
    pass

class PrintJob:
    def __init__(self, job_id, user, document_name, priority="normal"):
        self.job_id = job_id
        self.user = user
        self.document_name = document_name
        self.priority = priority

    def __str__(self):
        return f"[{self.job_id}] {self.document_name} by {self.user} ({self.priority})"


class SmartPrintQueue:
    def __init__(self):
        self.print_queue = Queue()
        self.undo_stack = []
        self.redo_stack = []

    def add_job(self, job):
        """
        Add a job to the print queue.
        Push the action to undo stack.
        """
        pass

    def cancel_job(self, job_id):
        """
        Cancel a job by job_id from the queue.
        Move removed job info to undo stack.
        """
        pass

    def undo_action(self):
        """
        Undo the last action (add/cancel).
        Move action to redo stack for redoing later.
        """
        pass

    def redo_action(self):
        """
        Redo the previously undone action.
        """
        pass

    def show_queue(self):
        """
        Display all pending print jobs in the queue.
        """
        pass

    def process_next_job(self):
        """
        Process the next available print job. 
        Urgent jobs should always be printed before normal ones.
        """
        pass

    def show_pending_jobs(self):
        """
        Display all pending jobs in both queues.
        """
        pass

    def show_completed_jobs(self):
        """
        Display all completed jobs.
        """
        pass


def menu():

    while True:
        print("\n===== 🖨️ SMART PRINT QUEUE MENU =====")
        print("1. Add Job")
        print("2. Cancel Job")
        print("3. Undo")
        print("4. Redo")
        print("5. Show Queue")
        print("6. Exit")

        # Add show pending/completed jobs options

        choice = input("Enter your choice: ")

        if choice == '1':
            # TODO: Take input for job details and call add_job()
            pass

        elif choice == '2':
            # TODO: Ask for Job ID and call cancel_job()
            pass

        elif choice == '3':
            # TODO: Call undo_action()
            pass

        elif choice == '4':
            # TODO: Call redo_action()
            pass

        elif choice == '5':
            # TODO: Call show_queue()
            pass

        elif choice == '6':
            print("Exiting Smart Print Queue System... 🖨️")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    menu()
```
