from abc import ABC, abstractmethod


class TechFactory(ABC):
    @abstractmethod
    def get_laptop(self):
        pass

    @abstractmethod
    def get_phone(self):
        pass


class SamsungFactory(TechFactory):
    def get_laptop(self):
        return SamsungLaptop()

    def get_phone(self):
        return SamsungPhone()


class AppleFactory(TechFactory):
    def get_laptop(self):
        return AppleLaptop()

    def get_phone(self):
        return ApplePhone()


class Laptop(ABC):
    def laptop_func(self):
        pass


class SamsungLaptop(Laptop):
    def laptop_func(self):
        return "Samsung"


class AppleLaptop(Laptop):
    def laptop_func(self):
        return "Apple"


class Phone(ABC):
    @abstractmethod
    def phone_func(self):
        pass

    @abstractmethod
    def another_phone_func(self, collab: Laptop):
        pass


class SamsungPhone(Phone):
    def phone_func(self):
        return "Samsung phone"

    def another_phone_func(self, collab: Laptop):
        result = collab.laptop_func()
        return f"This phone is the same brand as this laptop({result})"


class ApplePhone(Phone):
    def phone_func(self):
        return "Apple phone"

    def another_phone_func(self, collab: Laptop):
        result = collab.laptop_func()
        return f"This phone is the same brand as this laptop({result})"


def client_code(factory: TechFactory):

    product_a = factory.get_laptop()
    product_b = factory.get_phone()

    print(f"{product_b.phone_func()}")
    print(f"{product_b.another_phone_func(product_a)}", end="")


if __name__ == "__main__":

    print("Client: Testing client code with the Samsung factory type:")
    client_code(SamsungFactory())

    print("\n")

    print("Client: Testing the same client code with the Apple factory type:")
    client_code(AppleFactory())
    print("\n")
