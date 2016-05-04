import init


jdict = {"cirno": 9, "it's a string": True,
         ("tuple", "it is"): ("another", "one")}


def test_to_json():
    assert init.to_json.to_json(jdict) == """{["tuple","it is"]:["another","one"],"cirno":9,"it's a string":true}"""


def test_failed_to_json():
    assert init.to_json.to_json(jdict) == "not a json string"
