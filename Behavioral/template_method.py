from abc import ABC, abstractmethod


class WorkplaceCreator(ABC):

    def template_method(self):
        self.put_table()
        self.put_chair()
        self.put_computer()
        self.put_monitor()
        self.get_periphery()
        self.hook()
        self.stretch_electricity()
        self.stretch_net()

    def put_table(self):
        print('Set default desktop.')

    def put_chair(self):
        print('Install office chair on wheels')

    def stretch_net(self):
        print('Route the network cable from the nearest power outlet.')

    def stretch_electricity(self):
        print('Stretch power from the nearest source.')

    @abstractmethod
    def put_computer(self):
        pass

    @abstractmethod
    def put_monitor(self):
        pass

    @abstractmethod
    def get_periphery(self):
        pass

    def hook(self):
        pass


class ManagerWorkplace(WorkplaceCreator):

    def put_computer(self):
        print('Install a basic office computer to work with a browser and office software')

    def put_monitor(self):
        print('Install monitor 24" Full HD')

    def get_periphery(self):
        print('Install a standard keyboard and mouse SYNOLOGY B-100')


class DesignerWorkplace(WorkplaceCreator):

    def put_computer(self):
        print('Install a productive computer with a discrete graphics card')

    def put_monitor(self):
        print('Install QLED monitor 32" 3840х2160')

    def get_periphery(self):
        print('Install a basic mouse and a keyboard that is convenient for a particular programmer.')

    def hook(self):
        # put graphics tablet
        print('Also, the designer needs to install a graphics tablet.')


class ProgrammerWorkplace(WorkplaceCreator):

    def put_computer(self):
        print('Install a computer with a powerful processor and integrated graphics with two video outputs.')

    def put_monitor(self):
        print('Install 2 monitors (1 swivel) 24" Full HD')

    def get_periphery(self):
        print('Install a basic keyboard and mouse with high sensitivity and additional buttons.')


def client_code(data):
    data.template_method()


client_code(DesignerWorkplace())
