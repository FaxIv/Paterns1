from __future__ import annotations
from abc import ABC, abstractmethod


class UserInterface:
    def __init__(self, cloud: CloudTechnology):
        self.cloud = cloud

    def operation(self):
        return (f"Work result:"
                f"{self.cloud.cloud_api_operation()}")


class CloudTechnology(ABC):
    @abstractmethod
    def cloud_api_operation(self):
        pass


class GoogleCloud(CloudTechnology):
    def cloud_api_operation(self):
        return "Google cloud result"


class AppleCloud(CloudTechnology):
    def cloud_api_operation(self):
        return "Apple cloud result"


def client_code(user_interface: UserInterface):
    print(user_interface.operation())


if __name__ == "__main__":

    cloud = GoogleCloud()
    user_interface = UserInterface(cloud)
    client_code(user_interface)

    cloud = AppleCloud()
    user_interface = UserInterface(cloud)
    client_code(user_interface)
