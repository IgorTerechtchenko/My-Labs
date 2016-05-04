import re


def from_json(json_string):
    json_string = json_string.strip()
    jlist = re.compile("\[.*\]")
    jdict = re.compile("\{(.+:.+)+\}")
    jstring = re.compile("\".+\"|\'.+\'")
    jint = re.compile("-?[0-9]+")
    jt = re.compile("true")
    jf = re.compile("false")
    jfloat = re.compile(r"""([+-]?[1-9]+[0-9]*)?
                        [.]?[0-9]*([Ee][+-]?[0-9]+)?$""", re.X)
    jpair = re.compile("(?P<key>.+):(?P<value>.+)")
    if jdict.match(json_string):
        result = dict()
        json_string = json_string[:-1]
        json_string = json_string[1:]
        json_string = json_string.split(",")
        for el in json_string:
            pair = jpair.match(el)
            result.update({from_json(pair.group("key")): from_json(pair.group("value"))})
    elif jlist.match(json_string):
        result = []
        json_string = json_string[:-1]
        json_string = json_string[1:]
        json_string = json_string.split(",")
        for el in json_string:
            result.append(from_json(el))
    elif jstring.match(json_string):
        json_string = json_string[:-1]
        json_string = json_string[1:]
        result = json_string
    elif jfloat.match(json_string):
        result = float(json_string)
    elif jint.match(json_string):
        result = int(json_string)
    elif jt.match(json_string):
        result = True
    elif jf.match(json_string):
        result = False
    else:
        raise ValueError("Input is not a valid json string")
    return result

d = '{"da": "ze", "cirno": 9.0, "wow so json": true}'
f = from_json(d)
print f
print type(f)
