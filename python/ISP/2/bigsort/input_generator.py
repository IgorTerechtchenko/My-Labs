import random
import os
import sys


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


def write(file, section_separator="/", line_separator="\n",
          lines=1000000, sections=5, num=False):
        for x in range(lines):
            file.write(generate_line(section_separator, sections, num))
            file.write(line_separator)


def generate_file(afile, size=1000, section_separator="/", line_separator="\n",
                  lines=1000, sections=10, num=False):
    try:
        with open(afile, "w") as file:
            while os.path.getsize(afile) < size:
                write(file, section_separator, line_separator, lines, sections, num)
                print os.path.getsize(afile)
    except IOError:
        print "File {} doesn't exist".format(file)


def main():
    print sys.argv
    generate_file("f")
    # if len(sys.argv) > 4:
        # fsep = sys.argv[4]

    # if len(sys.argv) > 5:
        # lsep = sys.argv[5]

    # if len(sys.argv) >= 6:
        # num = sys.argv[6]

    # generate_file(str(sys.argv[1]), lines=int(sys.argv[2]), sections=int(sys.argv[3]), line_separator=lsep, section_separator=fsep, num=num)

if __name__ == "__main__":
    main()
