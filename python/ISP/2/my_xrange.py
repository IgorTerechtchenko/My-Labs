class MyXrange(object):
    def __init__(self, stop, start=0, step=1):
        self.stop = stop
        self.start = start
        self.step = step
        self.current_value = start
        self.iter_number = 0

    def __iter__(self):
        return self

    def next(self):
        if self.iter_number == 0:
            self.iter_number += 1
            return self.current_value
        self.current_value = self.current_value + self.step
        if self.current_value >= self.stop:
            raise StopIteration()
        return self.current_value

for x in MyXrange(100, 10, 5):
    print x

for x in MyXrange(10):
    print x
