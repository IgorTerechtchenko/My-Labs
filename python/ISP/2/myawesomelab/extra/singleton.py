class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Foo(object):
    __metaclass__ = Singleton

    def __init__(self, name):
        self.name = name


A = Foo("the one and only")
print A.name
print A
B = Foo("mere fake")
print B.name
print B
