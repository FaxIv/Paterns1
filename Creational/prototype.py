from copy import deepcopy
from abc import ABC, abstractmethod


class LaptopPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Laptop(LaptopPrototype):
    def __init__(self, design, price):
        self.design = design
        self.price = price

    def __str__(self):
        info: str = f"Laptop designed by {self.design} \n" \
                    f"Price: {self.price}$ \n"
        return info

    def clone(self):
        return deepcopy(self)


if __name__ == "__main__":
    laptop_samsung = Laptop("Samsung", 1000)
    print (laptop_samsung)

    laptop_apple = laptop_samsung.clone()
    laptop_apple.design = "Apple"
    laptop_apple.price = 1500
    print(laptop_apple)