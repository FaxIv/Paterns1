from abc import ABC, abstractmethod


class Instruction(ABC):
    @abstractmethod
    def make_inst(self):
        pass


class LaptopInstruction(Instruction):
    def make_inst(self):
        print('Laptop_instruction_text')


class PCInstruction(Instruction):
    def make_inst(self):
        print('PC_instruction_text')


class Choice(ABC):
    @abstractmethod
    def choice(self, type_):
        pass


class ChoiceInst(Choice):
    def choice(self, type_):
        if type_ == 'Laptop':
            return LaptopInstruction()
        elif type_ == 'PC':
            return PCInstruction()

if __name__ == '__main__':

    app = ChoiceInst()
    app.choice('Laptop').make_inst()
    app.choice('PC').make_inst()
