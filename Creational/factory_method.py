from abc import ABC, abstractmethod


class LaptopFactory(ABC):
    @abstractmethod
    def factory(self):
        pass


class SamsungFactory(LaptopFactory):
    def factory(self):
        return SamsungLaptop()


class AppleFactory(LaptopFactory):
    def factory(self):
        return AppleFactory()


class Laptop(ABC):
    @abstractmethod
    def create_operation(self):
        pass


class SamsungLaptop(Laptop):
    def create_operation(self):
        print('Laptop created by Samsung')
        pass


class AppleLaptop(Laptop):
    def create_operation(self):
        print('Laptop created by Apple')


if __name__ == '__main__':

    laptop = SamsungFactory()
    result = laptop.factory()
    print(result.create_operation())