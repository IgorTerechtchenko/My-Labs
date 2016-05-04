import init

x = []

for el in init.my_xrange.MyXrange(10):
    x.append(el)


def test_my_xrange():
    assert x[0] == 0


def test_failed_my_xrange():
    assert x[0] == 100
