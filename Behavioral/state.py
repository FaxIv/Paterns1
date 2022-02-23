from abc import ABC, abstractmethod


class PC:
    _state = None

    def __init__(self, state):
        self.transition(state)

    def transition(self, state):
        self._state = state
        self._state.context = self

    def press_space(self):
        self._state.space()

    def press_any_letter(self):
        self._state.letter()

    def press_enter(self):
        self._state.enter()


class State(ABC):
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @abstractmethod
    def space(self):
        pass

    @abstractmethod
    def letter(self):
        pass

    @abstractmethod
    def enter(self):
        pass


class StatePCBloc(State):
    def space(self):
        print('The PC is locked, when you press the space bar, nothing happens.')

    def letter(self):
        print('The specified letter is written in the password entry field.')

    def enter(self):
        print('Password verification. The PC opens the desktop (goes to the state StateBaseDesktop).\n')
        self.context.transition(StateBaseDesktop())


class StateBaseDesktop(State):
    def space(self):
        print('The desktop is open, when you press the space bar, nothing happens.')

    def letter(self):
        print('The pressed letter is entered into the search bar.')

    def enter(self):
        print('Opening a file or program found in the search bar (goes to the state StateCreateDocument)\n')
        self.context.transition(StateCreateDocument())


class StateCreateDocument(State):
    def space(self):
        print('Pressing the space bar inserts a space between words (letters).')

    def letter(self):
        print('Entering text.')

    def enter(self):
        print('Pressing enter, new line.')


context = PC(StatePCBloc())

context.press_space()
context.press_any_letter()
context.press_enter()

context.press_space()
context.press_any_letter()
context.press_enter()

context.press_space()
context.press_any_letter()
context.press_enter()

