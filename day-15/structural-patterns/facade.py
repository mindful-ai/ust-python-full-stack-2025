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

# Client
if __name__ == "__main__":
    computer = ComputerFacade()
    computer.start_computer()
