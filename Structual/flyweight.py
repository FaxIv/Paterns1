class ElectronicsFlyweight:

    def __init__(self, shared_data):
        self._shared_data = shared_data

    def operation(self, unique_data):
        print(f"Created {self._shared_data[1]} from {self._shared_data[0]} with these characteristics:\n"
              f"Diagonal: {unique_data[0]}\n"
              f"Display matrix: {unique_data[1]}\n"
              f"RAM: {unique_data[2]}\n"
              f"Memory: {unique_data[3]}\n")


class ElectronicsFactory:

    _electronics = {}

    def __init__(self, electronics_flyweight):
        for state in electronics_flyweight:
            self._electronics[self.get_key(state)] = ElectronicsFlyweight(state)

    def get_key(self, state):
        return "_".join(sorted(state))

    def get_flyweight_electronics(self, shared_data):
        key = self.get_key(shared_data)
        if not self._electronics.get(key):
            self._electronics[key] = ElectronicsFlyweight(shared_data)
        return self._electronics[key]

    def list_flyweight_electronics(self):
        count = len(self._electronics)
        print(f"ElectronicsFactory: I have {count} flyweight for created electronics")
        print("\n".join(map(str, self._electronics.keys())), end="")
        print("\n")


class ElectronicContext:
    def create_electronics(self, factory, creator, gadget_type, diagonal, display_matrix, ram, memory):
        flyweight = factory.get_flyweight_electronics([creator, gadget_type])
        flyweight.operation([diagonal, display_matrix, ram, memory])


factory = ElectronicsFactory([
    ["Samsung", "laptop"],
    ["Samsung", "TV"],
    ["Apple", "laptop"],
    ["Apple", "phone"],
])

factory.list_flyweight_electronics()

creator = ElectronicContext()

creator.create_electronics(factory, "Samsung", "laptop", "15.2", "IPS", "8 GB", "128 SSD")
creator.create_electronics(factory, "Samsung", "phone", "6.5", "IPS", "8 GB", "64 GB")

factory.list_flyweight_electronics()