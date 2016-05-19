def main():
    #  feels bad man
    n = int(raw_input())
    has_1021 = False
    has_1031 = False
    has_1033 = False
    has_1021_1031 = False
    has_1021_1033 = False
    has_1031_1033 = False
    for x in range(n):
        a = int(raw_input())
        if a == 1021:
            has_1021 = True
        elif a == 1031:
            has_1031 = True
        elif a == 1033:
            has_1033 = True
        elif a == 1021 * 1031:
            has_1021_1031 = True
        elif a == 1021 * 1033:
            has_1021_1033 = True
        elif a == 1031 * 1033:
            has_1031_1033 = True
        elif a == 1087388483:
            print "YES"
            return

    if has_1021 and has_1031 and has_1033:
        print "YES"
        return
    elif has_1021 and has_1031_1033:
        print "YES"
        return
    elif has_1031 and has_1021_1033:
        print "YES"
        return
    elif has_1033 and has_1021_1031:
        print "YES"
        return

    print "NO"

if __name__ == "__main__":
    main()
