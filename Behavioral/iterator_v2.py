from collections.abc import Iterable, Iterator
import random


class EarthIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._position = collection.index('forrest')
        self._forest = []
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
            self._forest.append(value)
        return self.curr_value

    def get_forest(self):
        forrest = len(self._forest)
        print(forrest)


class Earth(Iterable):

    def __init__(self):
        self._forest = []
        collection = [random.choice(['forrest', 'lava']) for x in range(20)]
        self._collection = collection

    def __iter__(self):
        return EarthIterator(self._collection)

    def get_collection(self):
        return self._collection


collect = Earth()


# print(collect.__iter__())
# collect.get_coll()
forest = []
print(len(collect))

# forest.append(c)