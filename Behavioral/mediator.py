from abc import ABC


class Mediator(ABC):
    def func(self, sender, target):
        pass


class ConcreteMediator(Mediator):

    def __init__(self, components):
        self._components = components
        for elem in self._components:
            elem.mediator = self

    def func(self, sender, target):
        if target == 'boss':
            return self.react_boss(sender)
        elif target == 'manager':
            return self.react_manager()
        else:
            return self.react_employee()

    def react_boss(self, sender):
        if sender != 'employee':
            return self._components[0].response()
        else:
            print('Boss can`t talk with employee')

    def react_manager(self):
        return self._components[1].response()

    def react_employee(self):
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
        print(f"Request by boss to {target} (can be for anyone)")
        self.mediator.func('boss', target)

    def response(self):
        print('Response by boss (can be only for managers)')


class Manager(BaseComponent):
    def request(self, target):
        print(f"Request by manager to {target} (can be for employee, manager or boss)")
        self.mediator.func('manager', target)

    def response(self):
        print('Response by manager (can be for anyone)')


class Employee(BaseComponent):
    def request(self, target):
        print(f"Request by employee to {target} (can be only for manager or another employee)")
        self.mediator.func('employee', target)

    def response(self):
        print('Response by employee (can be for anyone)')


c1 = Boss()
c2 = Manager()
c3 = Employee()
l1 = [c1, c2, c3]
mediator = ConcreteMediator(l1)
c3.request('manager')
