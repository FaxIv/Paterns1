from abc import ABC, abstractmethod


class DeviceAPI:
    def create_connection(self):
        print("Connection created")

    def get_info(self):
        print("Get information from device")


class Info:
    def formatting_info(self):
        print("Formatting information from the device in a convenient format")


class OutputToConsole:
    def output(self):
        print("Info output to console")


class CommandInterface(ABC):
    @abstractmethod
    def func(self):
        pass


class CreateConnectionCommand(CommandInterface):
    def __init__(self, executor):
        self._executor = executor

    def func(self):
        self._executor.create_connection()


class GetInfoCommand(CommandInterface):
    def __init__(self, executor):
        self._executor = executor

    def func(self):
        self._executor.get_info()


class FormattingCommand(CommandInterface):
    def __init__(self, executor):
        self._executor = executor

    def func(self):
        self._executor.formatting_info()


class OutputToConsoleCommand(CommandInterface):
    def __init__(self, executor):
        self._executor = executor

    def func(self):
        self._executor.output()


class Invoker:
    def __init__(self):
        self.history = []

    def add_command(self, command):
        self.history.append(command)

    def option(self):
        if self.history:
            for executor in self.history:
                executor.func()
        else:
            print("No command for execute")



api_object = DeviceAPI()
format_object = Info()
output_object = OutputToConsole()

invoker_class = Invoker()

invoker_class.add_command(CreateConnectionCommand(api_object))
invoker_class.add_command(GetInfoCommand(api_object))
invoker_class.add_command(FormattingCommand(format_object))
invoker_class.add_command(OutputToConsoleCommand(output_object))

invoker_class.option()




