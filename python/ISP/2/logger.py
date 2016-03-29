import inspect


class Logger(object):

    def __init__(self):
        self.x = 10
        self.log = []

    def my_sum(self, a, b):
        return a + b

    def __getattribute__(self, name):
        if inspect.ismethod(object.__getattribute__(self, name)) is True:
            def tmp(*args, **kwargs):
                res = object.__getattribute__(self, name)(*args, **kwargs)
                self.log.append((name, str(args), str(kwargs), res))
                return res
            return tmp
        else:
            return object.__getattribute__(self, name)

    def __str__(self):
        res = ""
        num = 1
        for msg in self.log:  # find out how to make string shorter
            res += "call number: {}; method name: {}; arguments: {}, {}; result: {}; \n".format(
                   num, msg[0], msg[1], msg[2], msg[3])  # is this codestyle right?
            num = num + 1
        return str(res)


class Sample_text(Logger):
    def sample(self):
        print "ayy lmao m8"

    def mul(self, a, b):
        return a * b


A = Logger()
print A.x

print A.my_sum(1, 2)
print A.my_sum(244, 88)
print A.my_sum(2, 17)
print A

B = Sample_text()
B.sample()
print B.mul(2, 10)
print B
