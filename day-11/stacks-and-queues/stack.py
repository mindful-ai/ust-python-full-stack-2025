from collections import deque

class Stack:

    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("Peek from empty stack")

    def is_empty(self):
        return len(self.stack) == 0
    
    def clear(self):
        self.stack.clear()

    def __repr__(self):
        return f"Stack({list(self.stack)})"
    

if __name__ == "__main__":

    # Undo/Redo functionality -> word processors, image editors, command history

    undo_stack = Stack()
    redo_stack = Stack()

    undo_stack.push("Typed Hello")
    undo_stack.push("Typed World")

    print("UNDO: ", undo_stack)

    # Undo the last action

    action = undo_stack.pop()
    redo_stack.push(action)

    print(f"Undo {action}")
    print("REDO : ", redo_stack)

    # Redo the undone action

    redo_action = redo_stack.pop()
    undo_stack.push(redo_action)

    print(f"Redo {redo_action}")