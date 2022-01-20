class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class NewSingleton(metaclass=Singleton):
    def some_func(self):
        pass

a = NewSingleton()
b = NewSingleton()

print(a)
print(b)

print(a is b)
