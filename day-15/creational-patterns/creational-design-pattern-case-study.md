# 🧩 Assessment: Creational Design Patterns  
### Patterns: Builder | Factory | Prototype | Singleton

---

## 🎯 Objective
Design and implement a **Smart Home Automation System** where different **devices** (like lights, fans, air conditioners, cameras, and sensors) can be **created, configured, and cloned** efficiently using appropriate **creational design patterns**.

---

## 🏠 Problem Context

A smart home system manages various smart devices. Each device may have:
- A name and model number  
- Power consumption details  
- Device type (e.g., Light, Fan, AC, Camera, Sensor)  
- Optional configurations (brightness, speed, temperature, sensitivity, etc.)

The system should support:
1. **Dynamic creation of devices** — without using direct constructors.  
2. **Configuration of devices step-by-step** (building customized device setups).  
3. **Cloning of existing devices** to quickly replicate settings.  
4. **A single global controller** to manage the system (Singleton pattern).

---

## 💡 Core Tasks

### 1️⃣ Factory Pattern  
Implement a `DeviceFactory` class that creates different device objects (`Light`, `Fan`, `AC`, etc.) based on input.

**Example:**
```python
DeviceFactory.create_device("Light")
```
This should return an instance of a `Light` object.

---

### 2️⃣ Builder Pattern  
Create a `DeviceBuilder` that configures complex devices step-by-step.  
For example, a **Smart AC** may require:
- Temperature setting  
- Cooling mode  
- Fan speed  
- Timer configuration  

**Expected usage:**
```python
builder = DeviceBuilder()
smart_ac = (builder.set_name("Bedroom AC")
                   .set_temp(24)
                   .set_mode("Cool")
                   .set_fan_speed("Medium")
                   .build())
```

---

### 3️⃣ Prototype Pattern  
Allow cloning of existing devices to quickly create similar ones with minor changes.

**Example:**
```python
living_room_light = DeviceFactory.create_device("Light")
bedroom_light = living_room_light.clone()
bedroom_light.name = "Bedroom Light"
```

---

### 4️⃣ Singleton Pattern  
Implement a `HomeController` class that ensures **only one instance** manages all devices.  
This controller should be responsible for:
- Registering new devices  
- Removing devices  
- Listing all devices in the system  

**Example:**
```python
controller = HomeController.get_instance()
controller.add_device(smart_ac)
controller.list_devices()
```

---

## 🧩 Integration Requirements

- Use **at least two** of the four creational patterns.  
- Demonstrate **object creation flexibility** without directly instantiating concrete classes.  
- Show **cloning**, **building**, or **centralized management** of devices.  
- Each pattern should be implemented in a separate class for clarity.

---

## 🧠 Bonus (Optional Enhancements)
- Save and load device configurations from a JSON file.  
- Add functionality to **turn devices ON/OFF**.  
- Print a structured summary of all registered devices from the Singleton controller.

---

## ✅ Sample Output (Illustrative)

```
HomeController instance created.
Device 'Living Room Light' created using Factory Pattern.
Device 'Living Room Light' cloned as 'Bedroom Light' using Prototype Pattern.
Smart AC configured using Builder Pattern.
All devices registered:
 - Living Room Light [Brightness: 80%]
 - Bedroom Light [Brightness: 80%]
 - Smart AC [Temp: 24°C, Mode: Cool]
```

---

## 📘 Submission Requirements

1. Python source code (`.py` file).  
2. Screenshot or console output demonstrating successful execution.  
3. Brief explanation (in comments or separate markdown) of which creational patterns were used and why.

---

## 🧭 Evaluation Criteria

| Criteria | Description | Marks |
|-----------|--------------|--------|
| Correct use of patterns | Appropriate and correct implementation of 2+ creational patterns | 30 |
| Code structure | Clarity, readability, and class-based design | 20 |
| Integration & functionality | Logical flow between Factory, Builder, Prototype, and Singleton | 30 |
| Output demonstration | Meaningful output, matches problem scenario | 10 |
| Bonus features | Optional enhancements implemented | 10 |

---

**Total Marks: 100**

---

### 💬 Hint
Think of this as how real smart home systems work — devices are created via a central control app (Factory), customized step-by-step (Builder), cloned for similar rooms (Prototype), and managed by one global hub (Singleton).

---
