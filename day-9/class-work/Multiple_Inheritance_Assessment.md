# 🧠 Python Assessment: Multiple Inheritance

## Problem Statement
Design and implement a **Smart Home Device Management System** using **multiple inheritance** in Python.

### Description
In a smart home environment, devices such as lights, speakers, and thermostats can be controlled remotely and connected via Wi-Fi.  
Your task is to design a system that demonstrates multiple inheritance concepts using the following guidelines:

- Define a **Device** base class with attributes and methods common to all devices.
- Define a **Connectable** base class for connectivity-related functionality.
- Create derived classes like **SmartLight**, **SmartSpeaker**, and **SmartThermostat** that inherit from both `Device` and `Connectable`.
- Implement a **SmartHome** manager class to manage all devices (add, show, turn on/off, connect Wi-Fi, etc.).
- Demonstrate the use of **Method Resolution Order (MRO)**.
- Include at least one overridden method (e.g., `__str__()` or `turn_on()`).
- This is an **object-oriented programming and multiple inheritance** exercise.

---

## 🧩 Starter Code (Skeleton)

```python
# ============================================================
# SMART HOME DEVICE MANAGEMENT SYSTEM  (Starter Code)
# Demonstrates Multiple Inheritance in Python
# ============================================================

class Device:
    """Base class representing a generic device."""

    def __init__(self, device_name):
        self.device_name = device_name
        self.status = "off"

    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Connectable:
    """Base class for connectivity features."""

    def __init__(self):
        self.wifi_connected = False

    def connect_wifi(self):
        pass

    def disconnect_wifi(self):
        pass


# ------------------------------------------------------------
# Derived Classes using Multiple Inheritance
# ------------------------------------------------------------

class SmartLight(Device, Connectable):
    """Derived class combining Device and Connectable"""

    def __init__(self, device_name, brightness=50):
        Device.__init__(self, device_name)
        Connectable.__init__(self)
        self.brightness = brightness

    def set_brightness(self, level):
        pass


class SmartSpeaker(Device, Connectable):
    """Derived class combining Device and Connectable"""

    def __init__(self, device_name, volume=5):
        Device.__init__(self, device_name)
        Connectable.__init__(self)
        self.volume = volume

    def set_volume(self, level):
        pass


class SmartThermostat(Device, Connectable):
    """Derived class combining Device and Connectable"""

    def __init__(self, device_name, temperature=24):
        Device.__init__(self, device_name)
        Connectable.__init__(self)
        self.temperature = temperature

    def set_temperature(self, temp):
        pass


# ------------------------------------------------------------
# Smart Home Manager Class
# ------------------------------------------------------------

class SmartHome:
    """Manages multiple smart devices."""

    def __init__(self):
        self.devices = []

    def add_device(self, device):
        pass

    def show_all_devices(self):
        pass

    def turn_all_on(self):
        pass

    def connect_all_wifi(self):
        pass


# ------------------------------------------------------------
# DEMONSTRATION AREA
# ------------------------------------------------------------

if __name__ == "__main__":
    # Create sample devices
    light = SmartLight("Living Room Light")
    speaker = SmartSpeaker("Home Speaker")
    thermostat = SmartThermostat("Bedroom Thermostat")

    # Add to SmartHome and perform basic operations
    home = SmartHome()
    home.add_device(light)
    home.add_device(speaker)
    home.add_device(thermostat)

    # Example: turn all devices on and connect Wi-Fi
    home.turn_all_on()
    home.connect_all_wifi()

    # Students can extend this to show all device details, etc.
```

---

### 🧠 Tasks for Students
1. Implement all `pass` methods with meaningful logic.  
2. Demonstrate multiple inheritance behavior using MRO (`SmartLight.mro()`).  
3. Use method overriding for device-specific behavior.  
4. Create at least three device instances and manage them through `SmartHome`.  
5. Display the final status of all devices.
