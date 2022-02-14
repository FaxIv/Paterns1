from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def attach(self, obs):
        pass

    @abstractmethod
    def detach(self, obs):
        pass

    @abstractmethod
    def notify(self):
        pass


class WaiterSubject(Subject):
    current_order = {}
    _employee_observers = []

    def attach(self, observ):
        print('Subject: Attached an observer.')
        self._employee_observers.append(observ)

    def detach(self, observ):
        self._employee_observers.remove(observ)

    def notify(self):
        for observ in self._employee_observers:
            observ.update(self)

    def get_order(self, order):
        print('Order created\n')
        self.current_order = order
        self.notify()


class EmployeeObserver(ABC):
    @abstractmethod
    def update(self, subject):
        pass


# class DishwasherObserver(EmployeeObserver):
#     def update(self, subject):
#         cup, plate
#         #     = subject.curent_order.get('dish')
#         # if dish:
#         #     return f''
#         # else:
#         #     pass
#

class CookObserver(EmployeeObserver):

    def update(self, subject):
        dish = subject.current_order.get('dish')
        if dish:
            print(f'Chef will cook {dish}')
        else:
            pass


class BartenderObserver(EmployeeObserver):

    def update(self, subject):
        drink = subject.current_order.get('drink')
        if drink:
            print(f'Bartender will cook {drink}')
        else:
            pass


order = {'dish': 'pasta', 'drink': 'beer'}

subject = WaiterSubject()

cook_observ = CookObserver()
bart_observ = BartenderObserver()

subject.attach(cook_observ)
subject.attach(bart_observ)
subject.get_order(order)



