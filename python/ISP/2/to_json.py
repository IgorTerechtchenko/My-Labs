def to_json(input, raise_unknown=False):
    class NonSerializableTypeError(TypeError):
        pass
    result = ""
    if isinstance(input, str):
        result += "\"" + input + "\""
    elif isinstance(input, (int, float)):
        result += str(input)
    elif isinstance(input, dict):
        result += "{"
        for key, value in input.iteritems():
            result += to_json(key) + ":" + to_json(value) + ","
        result = result[:-1]
        result += "}"
    elif isinstance(input, list) or isinstance(input, tuple):
        result += "["
        for element in input:
            result += to_json(element)
            result += ","
        result = result[:-1]
        result += "]"
    elif raise_unknown is True:
        raise NonSerializableTypeError("{} type is not serializable".format(str(type(input))))
    if result == "":
        return str(type(input))
    return result
