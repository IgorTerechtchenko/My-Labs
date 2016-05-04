import init


s = init.sequence.Sequence(range(10))


def test_filter():
    assert s.my_filter(lambda x: x % 2 == 0) == [0, 2, 4, 6, 8]


def test_failed_filter():
    assert s.my_filter(lambda x: x + 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
