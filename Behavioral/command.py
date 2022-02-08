from abc import ABC, abstractmethod


class CommandInterface(ABC):
    @abstractmethod
    def func(self):
        pass


class CreateFolderCommand(CommandInterface):
    def __init__(self, executor):
        self._executor = executor

    def func(self):
        self._executor.create_folder()


class OpenFolderCommand(CommandInterface):
    def __init__(self, executor):
        self._executor = executor

    def func(self):
        self._executor.open_folder()


class SaveFolderCommand(CommandInterface):
    def __init__(self, executor):
        self._executor = executor

    def func(self):
        self._executor.save_folder()


class DeleteFolderCommand(CommandInterface):
    def __init__(self, executor):
        self._executor = executor

    def func(self):
        self._executor.delete_folder()


class CreateNewOrOpenFolder:
    def create_folder(self):
        return "New folder created"

    def open_folder(self):
        return "Open folder"


class SaveFolder:
    def save_folder(self):
        return "Folder saved"


class DeleteFolder:
    def delete_folder(self):
        return "Folder deleted"
