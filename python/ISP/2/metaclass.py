def get_attrs(f):
    try:
        with open(f, "r") as file:
            attrs = file.read().split("\n")
    except IOError:
        print "File {} doesn't exist".format(file)
    del(attrs[-1])
    return attrs


class FileMeta(type):
    def __new__(cls, name, bases, attrs):
        cls.add = "abacaba"
        cls.a = 1
        for line in get_attrs("attrs"):
            exec("cls.{}".format(line))
        return super(FileMeta, cls).__new__(cls, name, bases, attrs)


class Foo(object):
    __metaclass__ = FileMeta

    def __init__(self):
        pass

a = Foo()
print Foo.add
print Foo.a
print Foo.b
print Foo.c
print Foo.odd(10)
