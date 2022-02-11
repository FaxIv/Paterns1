from abc import ABC


class Mediator(ABC):
    def func(self, sender, event):
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def func(self, sender, event):
        if event == 'manager':
            self._component2.response()
        else:
            self._component1.response()


class BaseComponent:
    def __init__(self):
        self._mediator = None

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator):
        self._mediator = mediator


class Manager(BaseComponent):

    def request_to1(self):
        print("Request by manager")
        self.mediator.func(self, 'manager')

    def response(self):
        print('Response by manager')


class Worker(BaseComponent):

    def request_to2(self):
        print('Request by worker')
        self.mediator.func(self, 'worker')

    def response(self):
        print('Response by worker')


c1 = Manager()
c2 = Worker()

mediator = ConcreteMediator(c1,c2)

c1.request_to1()