from abc import ABC, abstractmethod
import random


class EarthObject(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class Forest(EarthObject):

    def __init__(self, pos):
        self.position = pos

    def accept(self, visitor):
        visitor.visit_forest(self)


class Water(EarthObject):
    def __init__(self, pos):
        self.position = pos

    def accept(self, visitor):
        visitor.visit_water(self)


class Lava(EarthObject):
    def __init__(self, pos):
        self.position = pos

    def accept(self, visitor):
        visitor.visit_lava(self)


class Visitor(ABC):
    @abstractmethod
    def visit_forest(self, some_object):
        pass

    @abstractmethod
    def visit_water(self, some_object):
        pass

    @abstractmethod
    def visit_lava(self, some_object):
        pass


class NumAllObject(Visitor):
    def __init__(self):
        self._forest = []
        self._water = []
        self._lava = []

    def visit_forest(self, some_object):
        self._forest.append(some_object)

    def visit_water(self, some_object):
        self._water.append(some_object)

    def visit_lava(self, some_object):
        self._lava.append(some_object)

    def get_num(self):
        print(f"Number of forests: {len(self._forest)}\n"
              f"Number of water: {len(self._water)}\n"
              f"Number of lava: {len(self._lava)}")


class ForestPosition(Visitor):
    def __init__(self):
        self._map = []

    def visit_forest(self, some_object):
        s = some_object.position
        self._map.append(s)

    def visit_water(self, some_object):
        pass

    def visit_lava(self, some_object):
        pass

    def get_pos(self):
        result = self._map
        print(result)


class Earth:

    def __init__(self):
        self._collection = self.create_collection()

    def create_collection(self):
        collection = [random.choice([Forest(i), Water(i), Lava(i)]) for i in range(40)]
        return collection

    def get_elem(self, visitor):
        for elem in self._collection:
            elem.accept(visitor)

v1 = NumAllObject()
v2 = ForestPosition()
f = Earth()

f.get_elem(v1)
v1.get_num()
