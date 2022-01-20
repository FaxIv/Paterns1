from abc import ABC, abstractmethod
from enum import Enum, auto

class HardwareType(Enum):
    LowLevel = auto()
    AverageLevel = auto()
    HightLevel = auto()

class OperationSystem(Enum):
    MS_Windows = auto()
    Linux = auto()
    MacOS = auto()

class OtherSoftware(Enum):
    MS_Office = auto()
    Photoshop = auto()
    PyCharm = auto()


class Pc:
    def __init__(self, name):
        self.purpose = name
        self.hardware = None
        self.op_s = None
        self.software = None
    def __str__(self):
        info: str = f"Purpose PC: {self.purpose}\n " \
                    f"hardware: {self.hardware}\n" \
                    f"operation system: {self.op_s}\n " \
                    f"other software: {self.software}"
        return info


class Builder(ABC):

    @abstractmethod
    def choice_hardware(self) -> None: pass

    @abstractmethod
    def choice_os(self) -> None: pass

    @abstractmethod
    def add_software(self) -> None: pass

    @abstractmethod
    def get_pc(self) -> Pc: pass


class ManagerPCBuilder(Builder):
    def __init__(self):
        self.pc = Pc("For office manager")

    def choice_hardware(self) -> None:
        self.pc.hardware = HardwareType.LowLevel

    def choice_os(self) -> None:
        self.pc.op_s = OperationSystem.MS_Windows

    def add_software(self) -> None:
        self.pc.software = OtherSoftware.MS_Office

    def get_pc(self) -> Pc:
        return self.pc


class ProgramistPCBuilder(Builder):
    def __init__(self):
        self.pc = Pc("For programist")

    def choice_hardware(self) -> None:
        self.pc.hardware = HardwareType.AverageLevel

    def choice_os(self) -> None:
        self.pc.op_s = OperationSystem.Linux

    def add_software(self) -> None:
        self.pc.software = OtherSoftware.PyCharm

    def get_pc(self) -> Pc:
        return self.pc


class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builders: Builder):
        self.builder = builders

    def create_pc(self):
        if not self.builder:
            raise ValueError("Builder didn`t set")
        self.builder.choice_hardware()
        self.builder.choice_os()
        self.builder.add_software()


if __name__ == '__main__':
    director = Director()
    for pc in (ManagerPCBuilder, ProgramistPCBuilder):
        builder = pc()
        director.set_builder(builder)
        director.create_pc()
        pc = builder.get_pc()
        print(pc)