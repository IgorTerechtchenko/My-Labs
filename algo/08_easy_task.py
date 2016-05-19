#! /usr/bin/python

a = raw_input()
numbers = raw_input()

numbers = numbers.strip().split(" ")
inumbers = []

for x in numbers:
    inumbers.append(int(x))

for_max = inumbers[:]
max_mul = max(for_max)
for_max.remove(max_mul)
max_mul = max_mul * max(for_max)

min_mul = min(inumbers)
inumbers.remove(min_mul)
min_mul = min_mul * min(inumbers)

if max_mul > min_mul:
    print max_mul
else:
    print min_mul
