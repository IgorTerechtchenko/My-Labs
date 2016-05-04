import random
import sys


class BigInputGenerator(object):
    def __init__(self, filename, lines=10000, fields=5, line_separator="\n",
                 field_separator="/", numeric=False):
        if not filename:
            raise IOError("no file specified")
            sys.exit
        else:
            self.filename = filename
        self.lines = lines
        self.fields = fields
        self.line_separator = line_separator
        self.field_separator = field_separator
        self.numeric = numeric

    def __generate_field(self):
        field = ""
        if self.numeric is False:
            for x in range(3):
                field += unichr(random.randint(97, 122))
        elif self.numeric is True:
            for x in range(3):
                field += str(random.randint(0, 9))
        return field

    def __generate_line(self):
        line = ""
        for x in range(self.fields):
            line += self.field_separator
            line += self.__generate_field()
        line += self.field_separator
        return line

    def __write(self):
        if self.lines <= 100:
            buff = 1
        elif self.lines <= 1000:
            buff = 100
        else:
            buff = 1000
        try:
            f = open(self.filename, "w+r")
        except IOError:
            print "file doesn't exist"
            sys.exit()
        for x in range(self.lines / buff):
            tmp = ""
            for x in range(buff):
                tmp += self.__generate_line()
                tmp += self.line_separator
            f.write(tmp)
        f.close()

    def execute(self):
        self.__write()
