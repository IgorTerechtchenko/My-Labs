class Queue(object):
    def __init__(self, *args):
        self.s1 = list(args)
        self.s2 = []

    def enqueue(self, x):
        self.s1.append(x)

    def dequeue(self):
        if len(self.s2) == 0:
            if len(self.s1) == 0:
                raise IndexError("Queue is empty")
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())

        return self.s2.pop()


q = Queue(1, 2, 3, 4, 5)

q.enqueue(1488)
q.enqueue("adolf")
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
