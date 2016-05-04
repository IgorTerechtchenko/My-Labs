class MyDict(dict):
    def __init__(self, atype=None):
        if not callable(atype):
            raise TypeError("type must be callable")
        self.factory = atype
        self.type = atype

    def __missing__(self, key):
        try:
            val = self.factory(self.type)
        except TypeError:
            val = self.factory()
        self[key] = val
        return val


def main():
    D = MyDict(MyDict)
    D["da"]["ze"] = 9
    print D
