import copy

# ---------------------------
# Prototype Pattern
# ---------------------------
class Prototype:
    def clone(self):
        """Create a deep copy of the object"""
        return copy.deepcopy(self)


# ---------------------------
# Device Base Class
# ---------------------------
class Device(Prototype):
    def __init__(self, name, model, power):
        self.name = name
        self.model = model
        self.power = power

    def __str__(self):
        return f"{self.name} ({self.model}) - {self.power}W"


# ---------------------------
# Concrete Device Classes
# ---------------------------
class Light(Device):
    def __init__(self, name, model, power, brightness=100):
        super().__init__(name, model, power)
        self.brightness = brightness

    def __str__(self):
        return f"Light: {self.name} ({self.model}) - {self.power}W, Brightness: {self.brightness}%"


class Fan(Device):
    def __init__(self, name, model, power, speed=3):
        super().__init__(name, model, power)
        self.speed = speed

    def __str__(self):
        return f"Fan: {self.name} ({self.model}) - {self.power}W, Speed: {self.speed}"


class SmartAC(Device):
    def __init__(self, name, model, power, temperature=24, mode="Cool", fan_speed="Medium"):
        super().__init__(name, model, power)
        self.temperature = temperature
        self.mode = mode
        self.fan_speed = fan_speed

    def __str__(self):
        return (f"Smart AC: {self.name} ({self.model}) - {self.power}W, "
                f"Temp: {self.temperature}°C, Mode: {self.mode}, Fan Speed: {self.fan_speed}")


# ---------------------------
# Factory Pattern
# ---------------------------
class DeviceFactory:
    @staticmethod
    def create_device(device_type, name, model, power):
        """Creates device objects dynamically"""
        if device_type.lower() == "light":
            return Light(name, model, power)
        elif device_type.lower() == "fan":
            return Fan(name, model, power)
        elif device_type.lower() == "ac":
            return SmartAC(name, model, power)
        else:
            raise ValueError("Unknown device type!")


# ---------------------------
# Builder Pattern for SmartAC
# ---------------------------
class DeviceBuilder:
    def __init__(self):
        self.name = None
        self.model = None
        self.power = None
        self.temperature = 24
        self.mode = "Cool"
        self.fan_speed = "Medium"

    def set_name(self, name):
        self.name = name
        return self

    def set_model(self, model):
        self.model = model
        return self

    def set_power(self, power):
        self.power = power
        return self

    def set_temp(self, temperature):
        self.temperature = temperature
        return self

    def set_mode(self, mode):
        self.mode = mode
        return self

    def set_fan_speed(self, fan_speed):
        self.fan_speed = fan_speed
        return self

    def build(self):
        if not all([self.name, self.model, self.power]):
            raise ValueError("Name, model, and power must be specified!")
        return SmartAC(self.name, self.model, self.power, self.temperature, self.mode, self.fan_speed)


# ---------------------------
# Singleton Pattern
# ---------------------------
class HomeController:
    _instance = None

    def __init__(self):
        if HomeController._instance is not None:
            raise Exception("This class is a Singleton! Use get_instance().")
        self.devices = []
        # HomeController._instance = True
        print("HomeController instance created.")

    @staticmethod
    def get_instance():
        if HomeController._instance is None:
            HomeController._instance = HomeController()
        return HomeController._instance

    def add_device(self, device):
        self.devices.append(device)
        print(f"Added device: {device.name}")

    def list_devices(self):
        print("\n📋 Registered Devices:")
        for d in self.devices:
            print(" -", d)


# ---------------------------
# Client Code
# ---------------------------
if __name__ == "__main__":
    # Singleton Controller
    controller = HomeController.get_instance()

    # Factory Pattern
    living_room_light = DeviceFactory.create_device("Light", "Living Room Light", "Philips-Hue", 15)
    fan = DeviceFactory.create_device("Fan", "Ceiling Fan", "Usha-Breeze", 60)

    # Prototype Pattern - Clone existing device
    bedroom_light = living_room_light.clone()
    bedroom_light.name = "Bedroom Light"

    # Builder Pattern - Build complex SmartAC
    builder = DeviceBuilder()
    smart_ac = (builder.set_name("Bedroom AC")
                        .set_model("Daikin-X12")
                        .set_power(1500)
                        .set_temp(23)
                        .set_mode("Cool")
                        .set_fan_speed("High")
                        .build())

    # Add all devices to controller
    controller.add_device(living_room_light)
    controller.add_device(bedroom_light)
    controller.add_device(fan)
    controller.add_device(smart_ac)

    # List devices
    controller.list_devices()
