class DeviceAPI:
    def connection(self):
        return "Connected to device"

    def get_info(self):
        return "Get information from device"

    def check_connection(self):
        return True


class Info:
    def formatting_info(self):
        print("Formatting information from the device in a convenient format")


class WriteTextInFile:
    def write_text(self):
        print("Writing information to a file for analyzing logs")


class SystemFacade:
    def __init__(self, device_api, info, write_text):
        self._device_api = device_api
        self._info = info
        self._write_text = write_text

    def facade_func(self):
        if self._device_api.check_connection == True:
            return self._device_api.connection().get_info()


a = DeviceAPI()
b = Info()
c = WriteTextInFile()

client = SystemFacade(a, b, c)
print(client.facade_func())
