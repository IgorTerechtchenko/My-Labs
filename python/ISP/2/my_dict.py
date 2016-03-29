class MyDict(object):
    def __init__(self):
        self.ara = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]

    def __getitem__(self, key):
        MyDict.calls = 0
        MyDict.calls += 1
        if MyDict.calls % 2 != 0:
            MyDict.k = key
            return self.ara[key]
        else:
            return self.ara[key][key]
            MyDict.calls = 0

    def __setitem__(self, key, value):
        "is never actually called, dunno why"
        self.ara[key] = value
        return self

D = MyDict()

D[0][0] = 0
print D.ara
D[0][0] = 1
print D.ara
D[2][1] = 1148
print D.ara
