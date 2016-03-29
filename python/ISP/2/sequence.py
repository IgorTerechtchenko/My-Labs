# pretty shure i got this task wrong
class Sequence(object):
    def __init__(self, iterable_object):
        if hasattr(iterable_object, "__iter__"):
            self.seqence = iterable_object
        else:
            raise TypeError
        self.n = 0

    def __iter__(self):
        return self

    def next(self):
        try:
            return self.seqence[self.n]
        except IndexError:
            self.n = 0
            return self.seqence[self.n]
        finally:
            self.n += 1

    def my_filter(self, function):
        for x in self.seqence:
            print x  # TODO for some reason output is weird
            if function(x) is not True:
                self.seqence.remove(x)
        return self.seqence

v = Sequence(range(10))

print v.my_filter(lambda x: x % 2 == 0)
