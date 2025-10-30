# 🚦 State Machines in Python — Tutorial

## 🧩 What is a State Machine?

A **State Machine** (also called a *Finite State Machine*, FSM) is a design model used to represent an object that can be in one of a **finite number of states**, and its behavior changes depending on its current state.

It defines:
- **States** — distinct modes of behavior.
- **Transitions** — rules that define when and how you move from one state to another.
- **Events / Inputs** — triggers that cause state transitions.
- **Actions** — behaviors or outputs when entering, exiting, or during a state.

---

## 🧠 Real-world analogy: Elevator System

Think of an **Elevator** — it can be in one of these states:
- **Idle**
- **Moving Up**
- **Moving Down**
- **Maintenance**

Depending on its state, the elevator responds differently:
- If it’s **Idle**, it can start moving.
- If it’s **Moving**, it can’t take new passengers.
- If it’s **Maintenance**, it ignores all requests.

This behavior fits naturally with a **State Machine**.

---

## 🧱 Implementation using OOP in Python

We’ll use a simple **OOP-based state pattern** to model an Elevator State Machine.

```python
from abc import ABC, abstractmethod

# --- Abstract State ---
class ElevatorState(ABC):
    @abstractmethod
    def move_up(self, elevator):
        pass

    @abstractmethod
    def move_down(self, elevator):
        pass

    @abstractmethod
    def stop(self, elevator):
        pass


# --- Concrete States ---
class IdleState(ElevatorState):
    def move_up(self, elevator):
        print("Elevator starting to move up...")
        elevator.state = MovingUpState()

    def move_down(self, elevator):
        print("Elevator starting to move down...")
        elevator.state = MovingDownState()

    def stop(self, elevator):
        print("Elevator is already idle.")


class MovingUpState(ElevatorState):
    def move_up(self, elevator):
        print("Elevator already moving up.")

    def move_down(self, elevator):
        print("Elevator can't move down while going up.")
    
    def stop(self, elevator):
        print("Elevator stopping...")
        elevator.state = IdleState()


class MovingDownState(ElevatorState):
    def move_up(self, elevator):
        print("Elevator can't move up while going down.")
    
    def move_down(self, elevator):
        print("Elevator already moving down.")
    
    def stop(self, elevator):
        print("Elevator stopping...")
        elevator.state = IdleState()


class MaintenanceState(ElevatorState):
    def move_up(self, elevator):
        print("Cannot move up, elevator under maintenance.")
    
    def move_down(self, elevator):
        print("Cannot move down, elevator under maintenance.")
    
    def stop(self, elevator):
        print("Elevator remains in maintenance mode.")


# --- Context ---
class Elevator:
    def __init__(self):
        self.state = IdleState()
    
    def set_state(self, new_state):
        self.state = new_state

    def move_up(self):
        self.state.move_up(self)
    
    def move_down(self):
        self.state.move_down(self)
    
    def stop(self):
        self.state.stop(self)

    def maintenance_mode(self):
        print("Switching to maintenance mode...")
        self.state = MaintenanceState()


# --- Demo ---
if __name__ == "__main__":
    elevator = Elevator()

    elevator.move_up()       # Idle -> MovingUp
    elevator.move_down()     # Invalid transition
    elevator.stop()          # MovingUp -> Idle
    elevator.move_down()     # Idle -> MovingDown
    elevator.stop()          # MovingDown -> Idle
    elevator.maintenance_mode()
    elevator.move_up()       # Invalid, maintenance mode
```

---

## 🧾 Output (Illustrative)

```
Elevator starting to move up...
Elevator can't move down while going up.
Elevator stopping...
Elevator starting to move down...
Elevator stopping...
Switching to maintenance mode...
Cannot move up, elevator under maintenance.
```

---

## 💡 Why use a State Machine?

- **Improves maintainability** — no giant `if-else` blocks.
- **Encapsulates state logic** — each state is a class.
- **Scalable** — easy to add new states or transitions.
- **Realistic modeling** — perfect for simulations, workflows, game logic, or process management.

---

## 🏁 Summary

| Concept | Meaning |
|----------|----------|
| **State** | Defines object’s behavior at a specific time |
| **Transition** | Rule to move between states |
| **Event** | Trigger for transition |
| **Action** | Operation performed during or after transition |

---
