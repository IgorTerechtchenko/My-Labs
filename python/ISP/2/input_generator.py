import random
import os


def generate_field(num=False):
    field = ""
    if num is False:
        for x in range(3):
            field += unichr(random.randint(97, 122))
    elif num is True:
        for x in range(3):
            field += str(random.randint(0, 9))
    return field


def generate_line(field_separator, sections, num=False):
    line = ""
    for x in range(sections):
        line += field_separator
        line += generate_field(num)
    line += field_separator
    return line


def write(file, section_separator="\\", line_separator="\n",
          lines=1000000, sections=1000, num=False):
    x = 1
    try:
        for x in range(lines):
            file.write(generate_line(section_separator, sections, num))
            file.write(line_separator)
    except IOError:
        print "File {} doesn't exist".format(file)


def generate_file(afile, size=1000000, section_separator="\\", line_separator="\n",
                  lines=1000, sections=100, num=False):
    with open(afile, "w") as file:
        while os.path.getsize(afile) < size:
            write(file, section_separator, line_separator, lines, sections, num)
            print os.path.getsize(afile)


generate_file("f", lines=100, sections=10)
