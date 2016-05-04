import inspect


def StringField():
    return str


class ModelCreator(type):
    class NameDescriptor(object):
        def __init__(self, value, dtype):
            self.value = value
            self.dtype = dtype

        def __set__(self, name, value):
            print "set"
            if isinstance(value, self.dtype):
                self.name = value
            else:
                raise ValueError
            return None

        def __get__(self, name, dtype=None):
            print "get"
            return self.value

        def __str__(self):
            return str(self.value)

    def __init__(cls, name, bases, attrs):
        if "name" in attrs:
            ModelCreator.temp = attrs["name"]

    def __call__(self, *args, **kwargs):
        res = type.__call__(self, *args)
        for name in kwargs:
            if name == "name" and (isinstance(kwargs[name], ModelCreator.temp)):
                field = ModelCreator.NameDescriptor(kwargs[name], ModelCreator.temp)
                setattr(res, name, field)
        return res


class Test(object):
    __metaclass__ = ModelCreator
    name = StringField()


print t.name
print type(t.name)
print inspect.isdatadescriptor(t.name)
t.name = 123
print t.name
