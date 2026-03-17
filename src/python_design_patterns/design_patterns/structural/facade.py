"""
Facade Design Pattern | https://en.wikipedia.org/wiki/Facade_pattern

The Facade pattern provides a simplified interface to a complex subsystem, making it easier to use. It hides the complexity of the underlying system and exposes only what is necessary to the client.
"""

class CPU:
    def execute(self):
        return "CPU: Executing instructions..."

class Memory:
    def load(self, address: str, data: str):
        return f"Memory: Loading '{data}' at address {address}"

class HardDrive:
    def read(self, sector: int):
        return f"HardDrive: Reading sector {sector}"

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        results = []
        results.append(self.hard_drive.read(0))
        results.append(self.memory.load("0x00", "bootloader"))
        results.append(self.cpu.execute())
        return "\n".join(results)
