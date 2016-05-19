def main():
    string = list(raw_input())
    # checking if string includes more then one symbol
    for x in range(len(string)):
        try:
            tmp = string[x]
            if string[x + 1] != tmp:
                break
        except IndexError:
            print -1
            return

    while True:
        if string != string[::-1]:
            print len(string)
            return
        del(string[-1])

if __name__ == "__main__":
    main()
