# Behavioral Design Patterns in Python

This tutorial covers all **Behavioral Design Patterns** in detail — each with explanation, use case, and Python code examples.

---

## 🧩 1. Chain of Responsibility Pattern

### 📘 Concept
Allows a request to pass along a chain of handlers. Each handler decides whether to process the request or pass it to the next handler.

### 💼 Use Case
Consider an **IT support system** where different support levels handle different severity of issues.

### 💻 Python Example
```python
class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        raise NotImplementedError


class Level1Support(Handler):
    def handle(self, request):
        if request == "password reset":
            print("Level 1: Handled password reset.")
        elif self._successor:
            self._successor.handle(request)


class Level2Support(Handler):
    def handle(self, request):
        if request == "software installation":
            print("Level 2: Handled software installation.")
        elif self._successor:
            self._successor.handle(request)


class Level3Support(Handler):
    def handle(self, request):
        if request == "server down":
            print("Level 3: Handled server down issue.")
        else:
            print("Issue not handled.")


chain = Level1Support(Level2Support(Level3Support()))
chain.handle("software installation")
chain.handle("server down")
```

---

## 🧩 2. Command Pattern

### 📘 Concept
Encapsulates a request as an object, allowing parameterization, queuing, or undo functionality.

### 💼 Use Case
Undo/Redo feature in text editors.

### 💻 Python Example
```python
class Command:
    def execute(self):
        pass

    def undo(self):
        pass


class TextEditor:
    def __init__(self):
        self.text = ""

    def write(self, content):
        self.text += content

    def erase(self, length):
        self.text = self.text[:-length]


class WriteCommand(Command):
    def __init__(self, editor, content):
        self.editor = editor
        self.content = content

    def execute(self):
        self.editor.write(self.content)

    def undo(self):
        self.editor.erase(len(self.content))


editor = TextEditor()
cmd1 = WriteCommand(editor, "Hello ")
cmd2 = WriteCommand(editor, "World!")

cmd1.execute()
cmd2.execute()
print(editor.text)

cmd2.undo()
print("After undo:", editor.text)
```

---

## 🧩 3. Interpreter Pattern

### 📘 Concept
Defines a grammatical representation for a language and an interpreter to evaluate sentences in the language.

### 💼 Use Case
Evaluating simple mathematical or logical expressions.

### 💻 Python Example
```python
class Expression:
    def interpret(self):
        pass


class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self):
        return self.value


class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()


expr = Add(Number(5), Number(10))
print("Result:", expr.interpret())
```

---

## 🧩 4. Mediator Pattern

### 📘 Concept
Defines an object that encapsulates how a set of objects interact, promoting loose coupling.

### 💼 Use Case
Chat application where users communicate via a central ChatRoom.

### 💻 Python Example
```python
class ChatRoom:
    def show_message(self, user, message):
        print(f"[{user}] says: {message}")


class User:
    def __init__(self, name, chatroom):
        self.name = name
        self.chatroom = chatroom

    def send_message(self, message):
        self.chatroom.show_message(self.name, message)


chatroom = ChatRoom()
u1 = User("Alice", chatroom)
u2 = User("Bob", chatroom)

u1.send_message("Hello Bob!")
u2.send_message("Hey Alice!")
```

---

## 🧩 5. Memento Pattern

### 📘 Concept
Captures and restores an object’s state without exposing its internals.

### 💼 Use Case
Undo feature in text editors.

### 💻 Python Example
```python
class Memento:
    def __init__(self, state):
        self.state = state


class Editor:
    def __init__(self):
        self._text = ""

    def type(self, words):
        self._text += words

    def save(self):
        return Memento(self._text)

    def restore(self, memento):
        self._text = memento.state

    def show(self):
        print(self._text)


editor = Editor()
editor.type("Hello, ")
m1 = editor.save()

editor.type("World!")
m2 = editor.save()

editor.restore(m1)
editor.show()
```

---

## 🧩 6. Observer Pattern

### 📘 Concept
Defines a one-to-many dependency so that when one object changes state, all dependents are notified.

### 💼 Use Case
Stock market or weather updates.

### 💻 Python Example
```python
class Observer:
    def update(self, price):
        pass


class Stock:
    def __init__(self):
        self._observers = []
        self._price = 0

    def attach(self, observer):
        self._observers.append(observer)

    def set_price(self, price):
        self._price = price
        self._notify_all()

    def _notify_all(self):
        for obs in self._observers:
            obs.update(self._price)


class Investor(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, price):
        print(f"{self.name} notified. New stock price: {price}")


stock = Stock()
stock.attach(Investor("Alice"))
stock.attach(Investor("Bob"))

stock.set_price(120)
```

---

## 🧩 7. State Pattern

### 📘 Concept
Allows an object to change its behavior when its internal state changes.

### 💼 Use Case
ATM machine — behavior changes based on current state.

### 💻 Python Example
```python
class ATMState:
    def insert_card(self):
        pass


class NoCard(ATMState):
    def insert_card(self):
        print("Card inserted. Please enter PIN.")


class HasCard(ATMState):
    def insert_card(self):
        print("Card already inserted.")


class ATM:
    def __init__(self):
        self.state = NoCard()

    def set_state(self, state):
        self.state = state

    def insert_card(self):
        self.state.insert_card()


atm = ATM()
atm.insert_card()
atm.set_state(HasCard())
atm.insert_card()
```

---

## 🧩 8. Strategy Pattern

### 📘 Concept
Defines a family of algorithms, encapsulates each one, and makes them interchangeable.

### 💼 Use Case
Payment methods — credit card, PayPal, or cryptocurrency.

### 💻 Python Example
```python
class PaymentStrategy:
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")


class PaymentContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)


context = PaymentContext(CreditCardPayment())
context.pay(200)

context = PaymentContext(PayPalPayment())
context.pay(350)
```

---

## 🧩 9. Template Method Pattern

### 📘 Concept
Defines the skeleton of an algorithm in a method, deferring some steps to subclasses.

### 💼 Use Case
Data analysis pipeline — load → process → report.

### 💻 Python Example
```python
class DataProcessor:
    def process(self):
        self.load_data()
        self.analyze_data()
        self.report()

    def load_data(self):
        pass

    def analyze_data(self):
        pass

    def report(self):
        pass


class SalesDataProcessor(DataProcessor):
    def load_data(self):
        print("Loading sales data...")

    def analyze_data(self):
        print("Analyzing sales trends...")

    def report(self):
        print("Generating sales report...")


processor = SalesDataProcessor()
processor.process()
```

---

## 🧩 10. Visitor Pattern

### 📘 Concept
Allows adding new operations to objects without modifying their structure.

### 💼 Use Case
Tax or discount calculation on various product types.

### 💻 Python Example
```python
class Item:
    def accept(self, visitor):
        pass


class Book(Item):
    def accept(self, visitor):
        visitor.visit_book(self)


class Food(Item):
    def accept(self, visitor):
        visitor.visit_food(self)


class TaxVisitor:
    def visit_book(self, book):
        print("Book tax: 5%")

    def visit_food(self, food):
        print("Food tax: 10%")


items = [Book(), Food()]
visitor = TaxVisitor()

for item in items:
    item.accept(visitor)
```

---

## ✅ Summary Table

| Pattern | Core Idea | Example Use Case |
|----------|------------|-----------------|
| Chain of Responsibility | Pass request through handlers | Support ticket escalation |
| Command | Encapsulate requests as objects | Undo/redo |
| Interpreter | Define language grammar | Expression evaluator |
| Mediator | Central controller for communication | Chat room |
| Memento | Save/restore object state | Undo in editor |
| Observer | Notify dependents automatically | Stock market |
| State | Change behavior by state | ATM |
| Strategy | Select algorithm at runtime | Payment methods |
| Template | Define algorithm structure | Data processing |
| Visitor | Add operations without changing structure | Tax calculation |

---

**Author:** Purushotham Sannakariyappa  
**Topic:** Behavioral Design Patterns in Python
