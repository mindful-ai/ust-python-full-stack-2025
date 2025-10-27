
# 🚀 Linked Lists in Python — Complete Tutorial

## 🧩 Part 1: What is a Linked List?

A **Linked List** is a linear data structure where elements (called **nodes**) are **not stored in contiguous memory**.  
Each node contains:
1. **Data** – the value stored.
2. **Pointer (next)** – a reference to the next node.

Unlike Python lists (`list` type), linked lists:
- Allow efficient insertion and deletion anywhere.
- Do **not** require resizing or shifting elements.
- But have **slower random access** — must traverse sequentially.

---

## ⚙️ Part 2: Implementation of a Singly Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        curr = self.head
        if curr and curr.data == key:
            self.head = curr.next
            curr = None
            return

        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        if curr is None:
            return

        prev.next = curr.next
        curr = None

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")
```

### ✅ Example Usage

```python
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(5)

print("Linked List:")
ll.display()

ll.delete(20)
print("\nAfter deleting 20:")
ll.display()
```

---

## 🌍 Part 3: Realistic Use Case — Music Playlist

### 💡 Description

Imagine a **music player app** — you can play next, go back, and dynamically add songs.  
A **Doubly Linked List** fits perfectly for this.

```python
class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None
        self.prev = None


class MusicPlaylist:
    def __init__(self):
        self.current = None

    def add_song(self, title):
        new_song = SongNode(title)
        if self.current is None:
            self.current = new_song
            return

        last = self.current
        while last.next:
            last = last.next
        last.next = new_song
        new_song.prev = last

    def play_next(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print(f"▶ Now playing: {self.current.title}")
        else:
            print("🚫 End of playlist.")

    def play_previous(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            print(f"▶ Now playing: {self.current.title}")
        else:
            print("🚫 Start of playlist.")

    def show_playlist(self):
        temp = self.current
        while temp and temp.prev:
            temp = temp.prev

        print("🎵 Playlist:")
        while temp:
            print("   -", temp.title)
            temp = temp.next
```

### Example Usage

```python
playlist = MusicPlaylist()
playlist.add_song("Shape of You")
playlist.add_song("Perfect")
playlist.add_song("Castle on the Hill")
playlist.add_song("Photograph")

playlist.show_playlist()

print("\n▶ Starting playback...")
playlist.play_next()
playlist.play_next()
playlist.play_previous()
playlist.play_next()
playlist.play_next()
playlist.play_next()
```

---

## 🧠 Why Linked List Works Here

✅ Bidirectional traversal between songs.  
✅ Easy insertion/deletion of songs.  
✅ Can be extended to **Circular Playlist** (loops automatically).

---

## 🧩 Assessment: Task Manager using Linked List

### Problem Statement

Implement a **Task Manager** that manages user tasks using a **Singly Linked List**.  
Each node should store:
- Task name  
- Priority (High/Medium/Low)  
- Status (Pending/Completed)

Your program should:
1. Add a new task at the end.  
2. Display all tasks.  
3. Delete a task by name.  
4. Mark a task as completed.  
5. Count how many tasks are pending.

### Skeleton Code

```python
class TaskNode:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.status = "Pending"
        self.next = None


class TaskManager:
    def __init__(self):
        self.head = None

    def add_task(self, name, priority):
        pass

    def display_tasks(self):
        pass

    def delete_task(self, name):
        pass

    def mark_completed(self, name):
        pass

    def count_pending(self):
        pass


if __name__ == "__main__":
    manager = TaskManager()
    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Show Pending Task Count")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            priority = input("Enter priority (High/Medium/Low): ")
            manager.add_task(name, priority)
        elif choice == "2":
            manager.display_tasks()
        elif choice == "3":
            name = input("Enter task name to delete: ")
            manager.delete_task(name)
        elif choice == "4":
            name = input("Enter task name to mark completed: ")
            manager.mark_completed(name)
        elif choice == "5":
            print(f"Pending tasks: {manager.count_pending()}")
        elif choice == "6":
            print("Exiting Task Manager...")
            break
        else:
            print("Invalid choice. Try again.")
```

### Expected Output

```
===== TASK MANAGER =====
1. Add Task
2. Display Tasks
3. Delete Task
4. Mark Task as Completed
5. Show Pending Task Count
6. Exit

Enter choice: 1
Enter task name: Review report
Enter priority (High/Medium/Low): High

Enter choice: 1
Enter task name: Send email
Enter priority (High/Medium/Low): Medium

Enter choice: 2
Task: Review report | Priority: High | Status: Pending
Task: Send email | Priority: Medium | Status: Pending

Enter choice: 4
Enter task name to mark completed: Send email
Task marked as completed!

Enter choice: 5
Pending tasks: 1
```

---

## 🏁 Summary

| Operation | Time Complexity | Description |
|------------|----------------|--------------|
| Insert at beginning | O(1) | Just update head |
| Insert at end | O(n) | Traverse to last node |
| Delete a node | O(n) | Find the node first |
| Search | O(n) | Sequential traversal |
| Traverse | O(n) | Visit all nodes |

---

✅ **You learned:**
- How to build and traverse a linked list  
- A real-world playlist example  
- A task manager assessment project
