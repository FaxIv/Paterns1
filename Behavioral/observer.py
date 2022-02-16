from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def attach(self, observ):
        pass

    @abstractmethod
    def detach(self, observ):
        pass

    @abstractmethod
    def notify(self):
        pass


class WaiterSubject(Subject):
    _current_order = {}
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
        print('Waiter go to kitchen.\n')
        if order == {}:
            print('This visitor did not order anything')
        else:
            self._current_order = order
        self.notify()


class EmployeeObserver(ABC):
    @abstractmethod
    def update(self, subject):
        pass


class DishwasherObserver(EmployeeObserver):
    def update(self, subject):
        for elem in subject.current_order.keys():
            if elem == 'dish':
                print('Dishwasher prepared plate.')
            elif elem == 'drink':
                print('Dishwasher prepared cup.')
            else:
                return


class CookObserver(EmployeeObserver):

    def update(self, subject):
        dish = subject.current_order.get('dish')
        if dish:
            print(f'Chef will cook {dish}.')


class BartenderObserver(EmployeeObserver):

    def update(self, subject):
        drink = subject.current_order.get('drink')
        if drink:
            print(f'Bartender poured {drink}.')


order_1 = {}
order_2 = {'dish': 'pasta', 'drink': 'fresh'}
order_3 = {'dish': 'pizza'}

subject = WaiterSubject()

dish_observ = DishwasherObserver()
cook_observ = CookObserver()
bart_observ = BartenderObserver()

subject.attach(dish_observ)
subject.attach(cook_observ)
subject.attach(bart_observ)
print('\n')
subject.get_order(order_2)



