# Implementation interface
class Device:
    def turn_on(self): pass
    def turn_off(self): pass

# Concrete Implementations
class TV(Device):
    def turn_on(self): print("Turning on the TV")
    def turn_off(self): print("Turning off the TV")

class Radio(Device):
    def turn_on(self): print("Turning on the Radio")
    def turn_off(self): print("Turning off the Radio")

# Abstraction
class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def press_on(self):
        self.device.turn_on()

    def press_off(self):
        self.device.turn_off()

# Client
if __name__ == "__main__":
    tv_remote = RemoteControl(TV())
    radio_remote = RemoteControl(Radio())

    tv_remote.press_on()
    radio_remote.press_off()
