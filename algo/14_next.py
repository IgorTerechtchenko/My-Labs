def main():
    a = raw_input()
    ara = []
    for x in a:
        ara.append(x)
    if ara == sorted(ara)[::-1]:
        print -1
        return

    for x in range(len(ara)):
        suffix = ara[-x::]
        if suffix == sorted(suffix)[::-1]:
            ne_suffix = suffix
            ps = x
    prefix = ara[0:len(ara) - ps]

    for x in range(1, len(ne_suffix) + 1):
        if ne_suffix[-x] > prefix[-1]:
            tmp = prefix[-1]
            prefix[-1] = ne_suffix[-x]
            ne_suffix[-x] = tmp
            break

    prefix.append(sorted(ne_suffix))
    print "".join([item for sublist in prefix for item in sublist])

if __name__ == "__main__":
    main()
