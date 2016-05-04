import init


def test_get_length(setup):
    vtest = init.vector.init.vector.Vector(1, 2, 3, 4, 5)
    assert vtest.get_length() == 5


def test_failed_get_length(setup):
    vtest = init.vector.init.vector.Vector(1, 2, 3, 4, 5)
    assert vtest.get_length() == 100


def test_add():
    vtest = init.vector.Vector(1, 2, 3, 4, 5)
    decim_vector = init.vector.Vector(10, 10, 10, 10, 10)
    success_add = init.vector.Vector(11, 12, 13, 14, 15)
    assert vtest + decim_vector == success_add


def test_failed_add():
    vtest = init.vector.Vector(1, 2, 3, 4, 5)
    assert vtest + 5 == 5


def test_sub():
    vtest = init.vector.Vector(1, 2, 3, 4, 5)
    decim_vector = init.vector.Vector(10, 10, 10, 10, 10)
    success_add = init.vector.Vector(11, 12, 13, 14, 15)
    assert (success_add - decim_vector) == vtest


def test_failed_sub():
    vtest = init.vector.Vector(1, 2, 3, 4, 5)
    decim_vector = init.vector.Vector(10, 10, 10, 10, 10)
    assert decim_vector - vtest == 14


def test_eq():
    vtest = init.vector.Vector(1, 2, 3, 4, 5)
    vtest_copy = init.vector.Vector(1, 2, 3, 4, 5)
    assert (vtest == vtest_copy)


def test_failed_eq():
    vtest = init.vector.Vector(1, 2, 3, 4, 5)
    assert vtest == 11


def test_ne():
    vtest = init.vector.Vector(1, 2, 3, 4, 5)
    assert (vtest != 10)


def test_failed_ne():
    vtest = init.vector.Vector(1, 2, 3, 4, 5)
    assert vtest != vtest


def test_getitem():
    vtest = init.vector.Vector(1, 2, 3, 4, 5)
    assert vtest[0] == 1


def test_failed_getitem():
    vtest = init.vector.Vector(1, 2, 3, 4, 5)
    assert vtest[0] == 199


def test_str():
    vtest = init.vector.Vector(1, 2, 3, 4, 5)
    assert str(vtest) == "[1, 2, 3, 4, 5]"


def test_failed_str():
    vtest = init.vector.Vector(1, 2, 3, 4, 5)
    assert str(vtest) == "not a vector"


def test_repr():
    vtest = init.vector.Vector(1, 2, 3, 4, 5)
    assert repr(vtest) == "[1, 2, 3, 4, 5]"


def test_failed_repr():
    vtest = init.vector.Vector(1, 2, 3, 4, 5)
    assert repr(vtest) == 1
