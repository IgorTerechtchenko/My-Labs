#!/usr/bin/env python
# -*- coding: utf-8 -*-


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


@cached
def mul(a, b):
    return a * b


@cached
def inc(b, c=1, a=1):
    return b + a + c

print mul(5, 7)
print mul(10, 29134)
print mul(5, 7)

print inc(3, 2)
print inc(2, 10)
print inc(3, 2)
