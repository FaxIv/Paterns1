from __future__ import annotations

class Laptop():
    def operation(self):
        pass


class AppleLaptop(Laptop):
    def operation(self):
        return "Apple laptop"


class Decorator(Laptop):

    _laptop: Laptop = None

    def __init__(self, laptop: Laptop):
        self._laptop = laptop

    @property
    def component(self):
        return self._laptop

    def operation(self):
        return self._laptop.operation()


class FrameDecorator(Decorator):
    def operation(self):
        return f"{self.component.operation()} + gold color frame"


class MonitorDecorator(Decorator):
    def operation(self):
        return f"{self.component.operation()} + 2 inches to monitor"


def client_code(laptop: Laptop):
    print(f"RESULT: {laptop.operation()}", end="")

if __name__ == "__main__":
    simple_laptop = AppleLaptop()
    print("Client: I've got standard laptop")
    client_code(simple_laptop)
    print("\n")

    decorator1 = FrameDecorator(simple_laptop)
    decorator2 = MonitorDecorator(decorator1)
    print("Client: Now I've got a decorated laptop:")
    client_code(decorator2)
    print("\n")