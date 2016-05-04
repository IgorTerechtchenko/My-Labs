import inspect


class Logger(object):

    def __init__(self):
        self.x = 10
        self.log = []

    def my_sum(self, a, b):
        return a + b

    def __getattribute__(self, name):
        if inspect.ismethod(object.__getattribute__(self, name)):
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


def main():
    L = Logger()
    L.my_sum(1, 4)
    print L
