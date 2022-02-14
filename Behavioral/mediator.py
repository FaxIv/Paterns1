from abc import ABC


class Mediator(ABC):
    def func(self, sender, ev, target):
        pass


class ConcreteMediator(Mediator):

    def __init__(self, components):
        self._components = components
        for elem in self._components:
            elem.mediator = self

    def func(self, sender, ev, target):
        if target == 'boss':
            return self.boss(ev)
        elif target == 'manager':
            return self.manager()
        else:
            return self.employee()

    def boss(self, ev):
        if ev != 'employee':
            return self._components[0].response()
        else:
            print('Boss can`t talk with employee')

    def manager(self):
        return self._components[1].response()

    def employee(self):
        return self._components[2].response()


class BaseComponent:
    def __init__(self):
        self._mediator = None

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator):
        self._mediator = mediator


class Boss(BaseComponent):
    def request(self, target):
        print('Request by boss can be for anyone')
        self.mediator.func(self, 'boss', target)

    def response(self):
        print('Response by boss can be only for managers')


class Manager(BaseComponent):
    def request(self, target):
        print("Request by manager can be for employee, manager or boss")
        self.mediator.func(self, 'manager', target)

    def response(self):
        print('Response by manager can be for anyone')


class Employee(BaseComponent):
    def request(self, target):
        print('Request by employee can be only for manager or another employee')
        self.mediator.func(self, 'employee', target)

    def response(self):
        print('Response by employee can be for anyone')


c1 = Boss()
c2 = Manager()
c3 = Employee()
l1 = [c1, c2, c3]
mediator = ConcreteMediator(l1)
c3.request('employee')
