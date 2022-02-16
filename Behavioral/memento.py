from abc import ABC, abstractmethod


class GraphicsEditor:
    def __init__(self):
        self.current_size = 100
        self.current_contrast = 70
        self.current_brightness = 70
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
        self.current_size = self.state[0]
        self.current_contrast = self.state[1]
        self.current_brightness = self.state[2]

    def change_size(self, percent_size):
        self.current_size += percent_size

    def change_contrast(self, percent_contrast):
        self.current_contrast += percent_contrast

    def change_brightness(self, percent_brightness):
        self.current_brightness += percent_brightness

    # def cut_image(self, l, r, u, d):
    #     # left, right, up, down
    # def cut_image(self, cut_size):
    #     pass


class Memento(ABC):
    @abstractmethod
    def get_state(self):
        pass


class ConcreteMemento(Memento):
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Caretaker:
    def __init__(self, origin):
        self._save_states = []
        self._origin = origin

    def backup(self):
        self._save_states.append(self._origin.save_state())

    def undo(self):
        state = self._save_states.pop()
        self._origin.restore_state(state)


editor = GraphicsEditor()
backup_creator = Caretaker(editor)

editor.change_size(-5)
editor.change_contrast(-10)

backup_creator.backup()
print(editor.current_state())

editor.change_size(-50)
print(editor.current_state())

backup_creator.undo()
print(editor.current_state())







