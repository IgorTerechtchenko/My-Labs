import sys


def dfs(i, visitednodes, nodes):
    visitednodes[i] = True
    for node in nodes[i]:
        if not visitednodes[node]:
            dfs(node, visitednodes, nodes)


def main():
    inp = raw_input().split()
    n = int(inp[0])
    m = int(inp[1])
    subgraphs = 0
    nodes = [[] for i in range(n)]
    visitednodes = [False for i in range(n)]

    for i in range(m):
        s, e = raw_input().split()
        nodes[int(s) - 1].append(int(e) - 1)
        nodes[int(e) - 1].append(int(s) - 1)

    for i in range(n):
        if not visitednodes[i]:
            subgraphs += 1
            dfs(i, visitednodes, nodes)

    if subgraphs == 1:
        print m - (n - 1)

    elif subgraphs:
        print -1

    print subgraphs - 1


if __name__ == "__main__":
    sys.setrecursionlimit(100000000)
    main()
