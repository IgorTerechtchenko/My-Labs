def main():
    inp = raw_input().split(" ")
    if (abs(int(inp[2]) - int(inp[4])) == abs(int(inp[3]) - int(inp[5]))):
        print "NO"
    else:
        print "YES"

if __name__ == "__main__":
    main()
