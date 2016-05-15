def to_json(input, raise_unknown=False):
    class NonSerializableTypeError(TypeError):
        def __init__(self, type):
            self.type = type

        def __str__(self):
            return "{} type is not serializable".format(self.type)

    result = ""
    try:
        if isinstance(input, str):
            result += "\"" + input + "\""
        elif isinstance(input, bool):
            if input is True:
                result += "true"
            elif input is False:
                result += "false"
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
        elif raise_unknown:
            raise NonSerializableTypeError(type(input))
        if result == "":
            return str(type(input))
        return result
    except RuntimeError:
        raise ValueError("recursive object is not serializable")


def main():
    a1 = {}
    a2 = {'a1': a1}
    a1['a2'] = a2

    print to_json(a1)
    print type(to_json(a1))

if __name__ == "__main__":
    main()
