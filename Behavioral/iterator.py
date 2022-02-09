from collections.abc import Iterable, Iterator


class IteratorObject(Iterator):
    _position = None

    def __init__(self, collection):
        self._collection = collection
        self._position = 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()

        return value


class IterableObject(Iterable):

    def __init__(self, collection = []):
        self._collection = collection

    def __iter__(self):
        return IteratorObject(self._collection)

    def add_item(self, item):
        self._collection.append(item)


collection = IterableObject()
collection.add_item("Laptop")
collection.add_item("PC")
collection.add_item("Phone")
collection.add_item("Router")

print("\n".join(collection))
