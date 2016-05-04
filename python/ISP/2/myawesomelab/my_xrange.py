class MyXrange(object):
    def __init__(self, *args):
        if len(args) == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        elif len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        if self.step == 0:
            raise ValueError("step can't be 0")
        if (self.step < 0) and (self.start < self.stop):
            raise ValueError("invalid arguments")
        self.current_value = self.start
        self.iter_number = 1

    def __iter__(self):
        return self

    def next(self):
        self.current_value = self.start + self.step * (self.iter_number - 1)
        self.iter_number += 1
        if self.step > 0:
            if self.current_value > self.stop:
                raise StopIteration()
        else:
            if self.current_value < self.stop:
                raise StopIteration()
        return self.current_value


def main():
    for x in MyXrange(10):
        print x
