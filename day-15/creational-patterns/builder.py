# The builder help buld the complex objects step by step

'''
Computer(cpu="i9", ram="32GB", storage="1TB SSD", gpu="RTX 4090", os="Windows 11")

'''

class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None
        self.os = None

    def __str__(self):
        return f"CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}, GPU: {self.gpu}, OS: {self.os}"

# Builder Interface

from abc import ABC, abstractmethod

class ComputerBuilder(ABC):
    @abstractmethod
    def set_cpu(self): 
        pass

    @abstractmethod
    def set_ram(self): 
        pass

    @abstractmethod
    def set_storage(self): 
        pass

    @abstractmethod
    def set_gpu(self): 
        pass

    @abstractmethod
    def set_os(self): 
        pass

    @abstractmethod
    def get_computer(self): 
        pass


# Building a Gaming Computer

class GamingComputerBuilder(ComputerBuilder):

    def __init__(self):
        self.computer = Computer()

    def set_cpu(self):
        self.computer.cpu = "Intel Core i9"
        return self

    def set_ram(self):
        self.computer.ram = "32GB"
        return self

    def set_storage(self):
        self.computer.storage = "1TB NVMe SSD"
        return self

    def set_gpu(self):
        self.computer.gpu = "NVIDIA RTX 4090"
        return self

    def set_os(self):
        self.computer.os = "Windows 11 Pro"
        return self

    def get_computer(self):
        return self.computer

# Office Computer Builder

class OfficeComputerBuilder(ComputerBuilder):

    def __init__(self):
        self.computer = Computer()

    def set_cpu(self):
        self.computer.cpu = "Intel Core i5"
        return self

    def set_ram(self):
        self.computer.ram = "16GB"
        return self

    def set_storage(self):
        self.computer.storage = "512GB SSD"
        return self

    def set_gpu(self):
        self.computer.gpu = "Integrated Graphics"
        return self

    def set_os(self):
        self.computer.os = "Windows 11 Home"
        return self

    def get_computer(self):
        return self.computer

# Director class

class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct_computer(self):
        (self._builder
            .set_cpu()
            .set_ram()
            .set_storage()
            .set_gpu()
            .set_os())
        return self._builder.get_computer()

if __name__ == "__main__":
    # Build a Gaming Computer
    gaming_builder = GamingComputerBuilder()
    director = Director(gaming_builder)
    gaming_pc = director.construct_computer()
    print("Gaming PC:", gaming_pc)

    # Build an Office Computer
    office_builder = OfficeComputerBuilder()
    director = Director(office_builder)
    office_pc = director.construct_computer()
    print("Office PC:", office_pc)
