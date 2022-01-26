from __future__ import annotations


class Facade:

    def __init__(self, module1: Module1, module2: Module2):
        self._module1 = module1
        self._module2 = module2

    def func(self):
        results = []
        results.append(self._module1.func1_1())
        results.append(self._module2.func2_1())
        results.append(self._module1.func1_2())
        results.append(self._module2.func2_2())
        return "\n".join(results)


class Module1:
    def func1_1(self):
        return "Module 1: ready for work."
    def func1_2(self):
        return "Module 1: started."


class Module2:
    def func2_1(self):
        return "Module 2: ready for work."

    def func2_2(self):
        return "Module 2: started."


def client_code(facade: Facade):
    print(facade.func(), end="")


if __name__ == "__main__":
    module1 = Module1()
    module2 = Module2()
    facade = Facade(module1, module2)
    client_code(facade)
