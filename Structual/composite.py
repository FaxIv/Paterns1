from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def operation(self):
        pass


class SimpleLog(Component):
    def __init__(self, log_name):
        self.log_name = log_name

    def operation(self):
        return f"{self.log_name} log journal"


class ListOfLog(Component):

    def __init__(self, list_name):
        self.list_name = list_name
        self.children = []

    def add(self, log_component):
        self.children.append(log_component)

    def delete(self, log_component):
        self.children.remove(log_component)

    def operation(self):
        result = []
        for child in self.children:
            result.append(child.operation())
        return f"{self.list_name}: ({' / '.join(result)})"


list = ListOfLog("General list")
l1 = ListOfLog("SYSTEM LIST")
l2 = ListOfLog("KERNEL LIST")
sl1 = SimpleLog("Defender")
sl2 = SimpleLog("Error")
sl3 = SimpleLog("Power on/off")

list.add(l1)
list.add(l2)

l1.add(sl1)
l1.add(sl2)

l2.add(sl3)

print(sl1.operation())
print(list.operation())
