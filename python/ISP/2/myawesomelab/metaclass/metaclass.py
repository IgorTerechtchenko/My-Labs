def get_attrs(f):
    with open(f, "r") as file:
        attrs = file.read().split("\n")
    del(attrs[-1])
    return attrs


class FileMeta(type):
    def __new__(cls, name, bases, attrs):
        if "file_name" in attrs:
            for line in get_attrs(attrs["file_name"]):
                exec("cls.{}".format(line))
            del attrs["file_name"]
            return super(FileMeta, cls).__new__(cls, name, bases, attrs)
        else:
            raise IOError("no file passed")


class Foo(object):
    __metaclass__ = FileMeta
    file_name = "/home/pokapoka/coded/python/ISP/2/metaclass/attrs"

    def __init__(self):
        pass

a = Foo()
print Foo.a
print Foo.b
print Foo.c
print Foo.odd(10)
