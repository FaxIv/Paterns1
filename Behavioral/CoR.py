from abc import ABC, abstractmethod


class Interface(ABC):
    @abstractmethod
    def set_next(self, worker):
        pass

    @abstractmethod
    def func(self, request):
        pass


class BaseOption(Interface):
    _worker = None

    def set_next(self, worker):
        self._worker = worker
        return worker

    @abstractmethod
    def func(self, request):
        if self._worker:
            return self._worker.func(request)


class JsonOption(BaseOption):
    def func(self, request):
        if request == "json":
            return "Type JSON"
        else:
            return super().func(request)


class XmlOption(BaseOption):
    def func(self, request):
        if request == "xml":
            return "Type XML"
        else:
            return super().func(request)


def client_code(worker):
    result = worker.func('xml')
    print(result)


json = JsonOption()
xml = XmlOption()

json.set_next(xml)

client_code(json)
