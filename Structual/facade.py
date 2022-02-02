class DeviceAPI:
    def connection(self, device):
        print(f"Connected to device {device}")

    def get_info(self):
        print("Get information from device")

    def check_connection(self):
        return True


class Info:
    def formatting_info(self):
        print("Formatting information from the device in a convenient format")


class WriteTextInFile:
    def write_text(self):
        print("Writing information to a file for analyzing logs")


class SystemFacade:

    def create_connection(self, device_name):
        if DeviceAPI().check_connection() == True:
            return DeviceAPI().connection(device_name)

    def create_entry(self):
        DeviceAPI().get_info()
        Info().formatting_info()
        WriteTextInFile().write_text()



client = SystemFacade()
client.create_connection("Mikrotik")
client.create_entry()
print("\n")
