import init


d = init.my_dict.MyDict(init.my_dict.MyDict)
d["da"]["ze"] = 9


def test_my_dict():
    assert d["da"] == {"ze": 9}


def test_failed_my_dict():
    assert d["da"] == 11
