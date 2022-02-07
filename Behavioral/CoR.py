from abc import ABC, abstractmethod


class Interface(ABC):
    @abstractmethod
    def get_next(self):
        pass

    @abstractmethod
    def operation(self):
        pass


class AbstractProcessing(Interface):
    @abstractmethod
    def get_next(self):
        pass

    @abstractmethod
    def operation(self):
        pass
