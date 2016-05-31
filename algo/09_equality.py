n = raw_input()
llist = raw_input().strip().split(" ")
a = 0
last = 0
mmax = 0
ssum = 0

last = int(llist[0])
mmax = last
del(llist[0])

for a in llist:
    a = int(a)
    if a > mmax:
        ssum += (a - mmax)
        mmax = a
    else:
        if a < last:
            ssum += (last - a)
    last = a

print ssum
