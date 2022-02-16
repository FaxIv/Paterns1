from abc import ABC, abstractmethod
import random


class ProgramContext:
    def __init__(self, strategy, data):
        self._strategy = strategy
        self._data = data

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def data_operation(self):
        result = self._strategy.funk(self._data)
        return f"Initial data:\n" \
               f"{self._data}\n" \
               f"The result of the implementation of a specific strategy:\n" \
               f"{result}"


class StrategyInterface(ABC):
    @abstractmethod
    def funk(self, data):
        pass


class GetFirstElem(StrategyInterface):
    def funk(self, data):
        result = data[0]
        return result


class GetLen(StrategyInterface):
    def funk(self, data):
        result = len(data)
        return result


class Reverse(StrategyInterface):
    def funk(self, data):
        result = data[::-1]
        return result


inf = [1, 2, 3, 4, 5]

first_elem = GetFirstElem()
get_len = GetLen()
reverse = Reverse()

context = ProgramContext(reverse, inf)
concret_result = context.data_operation()
print(concret_result)
