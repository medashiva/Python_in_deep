'''

Singleton design pattern will make you create only one object

the second object will be none

    1) type is mandatory param to pass
    2) metaclass is mandatory to use singleton

'''

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args,**kwargs)
            return cls._instances[cls]


class A(metaclass=Singleton):
    def __init__(self):
        pass

class Z(metaclass=Singleton):
    def __init__(self):
        pass


a = A()
print(a)

b = A()
print(b)


z = Z()
print(z)
y = Z()
print(y)