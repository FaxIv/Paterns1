from collections.abc import Iterable, Iterator
import random


class EarthIterator(Iterator):
    _position = None
    forest = None

    def __init__(self, collection):
        self._collection = collection
        self._position = 0
        self.forest = []

    def __next__(self):
        try:
            # value = self._collection[self._position]

            if self._collection[self._position + 1] == 'lava':
                self._position += 2
            else:
                self._position += 1
                self.forest.append(value)

        except IndexError:
            raise StopIteration()
        return value
        # return self.forest

    def get_forest(self):
        print(self.forest)


class Earth(Iterable):

    def __init__(self):
        collection = [random.choice(['forest', 'lava']) for x in range(20)]
        self._collection = collection

    def __iter__(self):
        return EarthIterator(self._collection)

    def get_coll(self):
        print(self._collection)

collect = Earth()
# print(collect.__iter__())
# collect.get_coll()
print("\n".join(collect))