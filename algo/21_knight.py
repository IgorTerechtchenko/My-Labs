import sys
a = raw_input().split(" ")
n = int(a[0])
m = int(a[1])
i = int(a[2]) - 1
j = int(a[3]) - 1
if i == 0 and j == 0:
    print 0
    sys.exit()
field = [[float("inf") for o in range(n)] for p in range(m)]
field[0][0] = 0
queue = [(1, 1)]


def neigh(coords):
    z = 0
    g = 0
    a = [(1, 2), (-1, 2), (-2, 1), (-2, -1), (2, -1), (-1, -2), (1, -2), (2, 1)]
    neighbours = []
    for pair in a:
        z = coords[0] + pair[0]
        g = coords[1] + pair[1]
        if z > 0 and g > 0:
            neighbours.append((z, g))
    return neighbours


def bfs():
    tmp = queue.pop(0)
    # print "current: " + str(tmp)
    neighbours = neigh(tmp)
    counter = 1 + field[tmp[0] - 1][tmp[1] - 1]
    for pair in neighbours:
        try:
            if field[pair[0] - 1][pair[1] - 1] == float("inf"):
                if (pair[0] - 1 == j and pair[1] - 1 == i):
                    # for x in field:
                        # print x
                    print counter
                    sys.exit()
                field[pair[0] - 1][pair[1] - 1] = counter
                queue.append(pair)
        except IndexError:
            pass
        # print "neighbours: " + str(neighbours)
        # print "queue:" + str(queue)
        # for x in field:
            # print x


def main():
    while len(queue) > 0:
        bfs()
    # for x in field:
        # print x
    print "NEVAR"

if __name__ == "__main__":
    main()
