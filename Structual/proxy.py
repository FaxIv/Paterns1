from abc import ABC, abstractmethod
import datetime

class Interface(ABC):
    @abstractmethod
    def response(self):
        pass


class ServiceObject(Interface):
    def response(self):
        print("Response from service object")


class LogProxyService(Interface):

    log_num = []

    def __init__(self, service):
        self.service = service

    def response(self):
        self.service.response()
        self.log()
        print(self.log_num)

    def log(self):
        date = datetime.datetime.today().strftime("%H:%M:%S")
        info = f"Request to Service has been made {date}"
        self.log_num.append(info)


def client_code(service):
    service.response()


a = LogProxyService(ServiceObject())
client_code(a)






