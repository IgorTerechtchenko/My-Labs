class Sequence(object):
    class iter(object):
        def __init__(self, seq):
            self.seqence = seq
            self.n = 0

        def next(self):
            try:
                return self.seqence[self.n]
            except IndexError:
                raise StopIteration
            finally:
                self.n += 1

        def my_filter(self, function):
            for x in self.seqence:
                if function(x) is not True:
                    self.seqence.remove(x)
            return self.seqence

    def __init__(self, iterable_object):
        if hasattr(iterable_object, "__iter__"):
            self.seqence = iterable_object
        else:
            raise TypeError

    def __iter__(self):
        return Sequence.iter(self.seqence)

    def my_filter(self, function):
        return self.iter(self.seqence).my_filter(function)


def gen():
    cur = 5
    while True:
        yield cur
        cur += 1


def main():
    g = gen()
    S = Sequence(g)
    S.my_filter(lambda x: x % 2 == 0)

if __name__ == "__main__":
    main()
