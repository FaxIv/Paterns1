from abc import ABC, abstractmethod
from datetime import datetime


class GraphicsLibrary:
    def __init__(self, original):
        self.current_size = 100
        self.current_contrast = 100
        self.current_brightness = 100
        # self.original = original
        self.state = []

    def current_state(self):
        self.state = [self.current_size, self.current_contrast, self.current_brightness]
        return self.state

    def save_state(self):
        self.current_state()
        return ConcreteMemento(self.state)

    def restore_state(self, memento):
        self.state = memento.get_state()

    def change_size(self, percent_size):
        self.current_size += percent_size
        return self.current_size

    def change_contrast(self, percent_contrast):
        self.current_contrast += percent_contrast
        return self.current_contrast

    def change_brightness(self, percent_brightness):
        self.current_brightness += percent_brightness
        return self.current_brightness

    # def cut_image(self, l, r, u, d):
    #     # left, right, up, down
    # def cut_image(self, cut_size):
    #     pass


class Memento(ABC):
    @abstractmethod
    def get_state(self):
        pass

    @abstractmethod
    def get_date(self):
        pass


class ConcreteMemento(Memento):
    def __init__(self, state):
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self):
        return self._state

    def get_date(self):
        return self._date


class CommandInterface(ABC):
    @abstractmethod
    def func(self, data):
        pass


class ChangeSizeInPercent(CommandInterface):
    def __init__(self, executor):
        self._executor = executor

    def func(self, data):
        self._executor.save_state()
        self._executor.change_size(data)


class ChangeContrast(CommandInterface):
    def __init__(self, executor):
        self._executor = executor

    def func(self, data):
        self._executor.save_state()
        self._executor.change_contrast(data)


class ChangeBrightness(CommandInterface):
    def __init__(self, executor):
        self._executor = executor

    def func(self, data):
        self._executor.save_state()
        self._executor.change_brightness(data)


# class CutImage(CommandInterface):
#     def __init__(self, executor):
#         self._executor = executor
#
#     def func(self, data):
#         self._executor.cut_image(data)

