from collections.abc import Iterable, Iterator
import random


class EarthIterator(Iterator):

    def __init__(self, collection):
        self._collection = collection
        self._position = 0
        self._curr_value = None

    def __next__(self):
        try:
            value = self._collection[self._position]
        except IndexError:
            raise StopIteration()

        if value == 'lava':
            self._position += 2
        else:
            self._position += 1
            self.curr_value = value

        return self.curr_value


class Earth(Iterable):

    def __init__(self):
        self._forrest = []
        self._collection = []
        for x in range(10):
            for i in range(random.randint(1, 9)):
                self._collection.append('forrest')
            self._collection.extend(['lava', 'lava'])

    def __iter__(self):
        return EarthIterator(self._collection)

    def get_forrest(self):
        for elem in self:
            self._forrest.append(elem)
        return len(self._forrest)


collect = Earth()
print(collect.get_forrest())
