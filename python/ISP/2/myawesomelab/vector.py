class Vector(object):
    class NotSupportedOperand(TypeError):
        pass

    class LengthNotEqual(ValueError):
        pass

    def __init__(self, *args):
        self.values_list = []
        for x in args:
            if isinstance(x, (float, int)):
                    self.values_list.append(x)

    def get_length(self):
        result = 0
        for x in self.values_list:
            result += 1
        return result

    def __add__(self, vector):
        if isinstance(vector, Vector):
            if self.get_length() == vector.get_length():
                new_list = []
                for x in range(self.get_length()):
                    new_list.append(self.values_list[x] + vector.values_list[x])
                self.values_list = new_list
                return self
            else:
                raise Vector.LengthNotEqual()
        else:
            raise Vector.NotSupportedOperand()

    def __sub__(self, vector):
        if isinstance(vector, Vector):
            if self.get_length() == vector.get_length():
                new_list = []
                for x in range(self.get_length()):
                    new_list.append(self.values_list[x] - vector.values_list[x])
                self.values_list = new_list
                return self
            else:
                raise Vector.LengthNotEqual()
        else:
            raise Vector.NotSupportedOperand()

    def __mul__(self, input):
        if isinstance(input, (int, float)):
            self.values_list = map(lambda x: x * input, self.values_list)
            return self
        elif isinstance(input, Vector):
            if self.get_length() == input.get_length():
                new_list = []
                for x in range(self.get_length()):
                    new_list.append(self.values_list[x] * input.values_list[x])
                self.values_list = new_list
                return self
            else:
                raise Vector.LengthNotEqual()
        else:
            raise Vector.NotSupportedOperand()

    def __eq__(self, input):
        if isinstance(input, Vector):
            if self.values_list == input.values_list:
                return True
        elif isinstance(input, (int, float)) & (self.get_length() == 1):
            if self.values_list[0] == input:
                return True
        return False

    def __ne__(self, input):  # super lazy edition
        if self.__eq__(input):
            return False
        else:
            return True

    def __getitem__(self, n):
        return self.values_list[n]

    def __str__(self):
        return str(self.values_list)

    def __repr__(self):
        return str(self.values_list)


def main():
    v = Vector(1, 2, 3, 5)
    print v
    print type(v)
