def cached(func):
    cache = dict()

    def tmp(*args, **kwargs):
        if args in cache:
            print "using cached values"
            return cache[args]
        res = func(*args, **kwargs)
        cache[args] = res
        return res
    return tmp


def main():
    @cached
    def mul(a, b):
        return a * b

    @cached
    def inc(b, c=1, a=1):
        return b + a + c

    @cached
    def a(a):
        return a ** 1000000

    a(2)
    a(2)
