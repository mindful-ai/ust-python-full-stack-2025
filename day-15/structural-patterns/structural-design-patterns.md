# 🧱 Structural Design Patterns in Python

Structural design patterns are concerned with how classes and objects are composed to form larger structures.  
They help ensure that if one part of a system changes, the entire system does not need to change.

---

## 📚 Patterns Covered

1. Adapter Pattern  
2. Bridge Pattern  
3. Composite Pattern  
4. Decorator Pattern  
5. Facade Pattern  
6. Flyweight Pattern  
7. Proxy Pattern

---

## 🧩 1. Adapter Pattern

### **Purpose**
The Adapter Pattern allows two incompatible interfaces to work together.  
It acts as a bridge between an existing class and a new interface.

### **Real-world Analogy**
You have a laptop with a USB-C port, but your old mouse has a USB-A connector — you use an *adapter*.

### **Example: Integrating a JSON-based Logger with an XML-based System**

```python
# Existing class (incompatible interface)
class XMLLogger:
    def log_xml(self, xml_data):
        print(f"Logging data in XML format: {xml_data}")

# Target interface expected by our application
class JSONLoggerInterface:
    def log(self, data):
        pass

# Adapter to convert JSON data to XML format
class JSONtoXMLAdapter(JSONLoggerInterface):
    def __init__(self, xml_logger):
        self.xml_logger = xml_logger

    def log(self, data):
        xml_data = "<log>" + "".join([f"<{k}>{v}</{k}>" for k, v in data.items()]) + "</log>"
        self.xml_logger.log_xml(xml_data)

# Client code
if __name__ == "__main__":
    xml_logger = XMLLogger()
    adapter = JSONtoXMLAdapter(xml_logger)
    log_data = {"event": "login", "user": "admin"}
    adapter.log(log_data)
```

---

## 🌉 2. Bridge Pattern

### **Purpose**
Decouples an abstraction from its implementation, allowing both to vary independently.

### **Example: Remote Control for Devices**

```python
class Device:
    def turn_on(self): pass
    def turn_off(self): pass

class TV(Device):
    def turn_on(self): print("Turning on the TV")
    def turn_off(self): print("Turning off the TV")

class Radio(Device):
    def turn_on(self): print("Turning on the Radio")
    def turn_off(self): print("Turning off the Radio")

class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def press_on(self):
        self.device.turn_on()

    def press_off(self):
        self.device.turn_off()

if __name__ == "__main__":
    tv_remote = RemoteControl(TV())
    radio_remote = RemoteControl(Radio())
    tv_remote.press_on()
    radio_remote.press_off()
```

---

## 🌳 3. Composite Pattern

### **Purpose**
Treat individual objects and compositions of objects uniformly.  
Useful for tree structures (e.g., folders, menus).

### **Example: File System Hierarchy**

```python
class FileComponent:
    def show_details(self):
        pass

class File(FileComponent):
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print(f"File: {self.name}")

class Folder(FileComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileComponent):
        self.children.append(component)

    def show_details(self):
        print(f"Folder: {self.name}")
        for child in self.children:
            child.show_details()

if __name__ == "__main__":
    file1 = File("resume.docx")
    file2 = File("photo.jpg")
    subfolder = Folder("Documents")
    subfolder.add(file1)
    subfolder.add(file2)

    main_folder = Folder("Desktop")
    main_folder.add(subfolder)
    main_folder.add(File("notes.txt"))
    main_folder.show_details()
```

---

## 🎨 4. Decorator Pattern

### **Purpose**
Add new functionality to an object dynamically without altering its structure.

### **Example: Coffee with Add-ons**

```python
class Coffee:
    def cost(self):
        return 50

class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 10

class SugarDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 5

if __name__ == "__main__":
    basic_coffee = Coffee()
    milk_coffee = MilkDecorator(basic_coffee)
    sugar_milk_coffee = SugarDecorator(milk_coffee)
    print("Total Cost:", sugar_milk_coffee.cost())
```

---

## 🏢 5. Facade Pattern

### **Purpose**
Provides a simplified interface to a complex subsystem.

### **Example: Computer Startup**

```python
class CPU:
    def start(self): print("CPU started")

class Memory:
    def load(self): print("Memory loaded")

class Disk:
    def spin(self): print("Disk spinning")

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.disk = Disk()

    def start_computer(self):
        self.cpu.start()
        self.memory.load()
        self.disk.spin()
        print("Computer started successfully!")

if __name__ == "__main__":
    computer = ComputerFacade()
    computer.start_computer()
```

---

## 🪶 6. Flyweight Pattern

### **Purpose**
Reduces memory usage by sharing common data between multiple similar objects.

### **Example: Trees in a Forest Simulation**

```python
class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def display(self, x, y):
        print(f"Drawing {self.name} tree at ({x},{y}) with color {self.color}")

class TreeFactory:
    _tree_types = {}

    @staticmethod
    def get_tree_type(name, color, texture):
        key = (name, color, texture)
        if key not in TreeFactory._tree_types:
            TreeFactory._tree_types[key] = TreeType(name, color, texture)
        return TreeFactory._tree_types[key]

class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def display(self):
        self.tree_type.display(self.x, self.y)

if __name__ == "__main__":
    forest = []
    for i in range(5):
        tree_type = TreeFactory.get_tree_type("Pine", "Green", "Rough")
        forest.append(Tree(i * 10, i * 5, tree_type))

    for tree in forest:
        tree.display()
```

---

## 🧱 7. Proxy Pattern

### **Purpose**
Controls access to another object, adding functionality like caching or lazy initialization.

### **Example: Virtual Proxy for Image Loading**

```python
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

if __name__ == "__main__":
    image = ProxyImage("photo.png")
    print("First call:")
    image.display()
    print("\nSecond call:")
    image.display()
```

---

# 🧠 Assessment Problems for Structural Design Patterns

Below are practical assignments for applying the concepts learned above.

---

## 🧩 Adapter Pattern — *Integrating Legacy Payment System*
**Context:** A legacy payment system only supports USD, but the new app must handle multiple currencies.  
**Challenge:** Implement an adapter that converts any currency into USD before passing it to the legacy system.  
**Expected Outcome:** Integrate old and new systems without modifying legacy code.

---

## 🌉 Bridge Pattern — *Controlling Multiple Smart Devices*
**Context:** A smart home controller app manages multiple devices (TV, Lights, Speaker) using different protocols.  
**Challenge:** Decouple device abstraction from communication implementation using the Bridge Pattern.  
**Expected Outcome:** Add new devices or protocols independently.

---

## 🌳 Composite Pattern — *Organization Hierarchy Viewer*
**Context:** Build an HR tool to visualize departments and employees.  
**Challenge:** Represent both Employees and Departments uniformly using the Composite Pattern.  
**Expected Outcome:** Display organization hierarchy recursively.

---

## 🎨 Decorator Pattern — *Dynamic Report Generation*
**Context:** A reporting system supports dynamic add-ons like charts, watermarks, and timestamps.  
**Challenge:** Add these features dynamically using decorators, without altering base code.  
**Expected Outcome:** Combine decorators for flexible report output.

---

## 🧱 Proxy Pattern — *Image Loading Optimization*
**Context:** A photo gallery loads images from a server, but loading is slow.  
**Challenge:** Implement a Virtual Proxy that loads images only when displayed.  
**Expected Outcome:** Reduce load time by lazy-loading images.
