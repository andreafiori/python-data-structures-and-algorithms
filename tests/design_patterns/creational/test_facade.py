from python_design_patterns.design_patterns.structural.facade import ComputerFacade, HardDrive, Memory, CPU

class TestFacadePattern:
    def test_cpu_execute(self):
        cpu = CPU()
        assert cpu.execute() == "CPU: Executing instructions..."

    def test_memory_load(self):
        memory = Memory()
        assert memory.load("0x00", "bootloader") == "Memory: Loading 'bootloader' at address 0x00"

    def test_hard_drive_read(self):
        hard_drive = HardDrive()
        assert hard_drive.read(0) == "HardDrive: Reading sector 0"

    def test_computer_facade_start(self):
        facade = ComputerFacade()
        result = facade.start()
        assert "HardDrive: Reading sector 0" in result
        assert "Memory: Loading 'bootloader' at address 0x00" in result
        assert "CPU: Executing instructions..." in result
