from tempfile import TemporaryFile
from sys import exit


class BigSort(object):
    def __init__(self, input_file, output_file, line_separator="\n", field_separator="/",
                 buffer_size=100, m_fields=(), numeric=False, reverse=False, check=False):
        self.input_file = input_file
        self.output_file = output_file
        self.line_separator = line_separator
        self.field_separator = field_separator
        self.buffer_size = buffer_size
        self.m_fields = m_fields
        self.numeric = numeric
        self.reverse = reverse
        self.check = check

    def execute(self):
        if not self.check:
            chunks = self.__make_chunks()
            self.__merge(chunks)
        elif self.check:
            return self.__check()

    def __make_chunks(self):
        """split a [inp] file into [size] of sorted chunks
           stored in a list of tempfiles"""
        files = []
        with open(self.input_file, "r") as read:
            while True:
                t = ""
                tmp = TemporaryFile()
                for line in range(self.buffer_size):
                    x = self.__readline(read)
                    if not x:
                        return files
                    t += x
                    read.seek(len(x), 1)
                t = self.__sort(t)
                tmp.write(t)
                tmp.seek(0)
                files.append(tmp)

    def __sort(self, llist):
        "sort a string of lines"
        newlist = []

        llist = llist.split(self.line_separator)
        del(llist[-1])
        del(llist[-1])
        for l in llist:
            newlist.append(l.split(self.field_separator))
        for l in newlist:
            del(l[0])
            del(l[-1])

        newlist = self.__merge_sort(newlist, self.m_fields)
        return self.__restore(newlist)

    def __merge_sort(self, alist, m_fields):
        """implementation of mergesort by [el]
           helper function for sort()"""
        if len(alist) > 1:
            mid = len(alist) // 2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            self.__merge_sort(lefthalf, self.m_fields)
            self.__merge_sort(righthalf, self.m_fields)

            i = 0
            j = 0
            k = 0

            while i < len(lefthalf) and j < len(righthalf):
                # if lefthalf[i][self.m_field] < righthalf[j][self.m_field]:
                if lefthalf[i] < righthalf[j]:
                    alist[k] = lefthalf[i]
                    i += 1
                else:
                    alist[k] = righthalf[j]
                    j += 1
                k += 1

            while i < len(lefthalf):
                alist[k] = lefthalf[i]
                i += 1
                k += 1

            while j < len(righthalf):
                alist[k] = righthalf[j]
                j += 1
                k += 1
        return alist

    def __restore(self, sorted_list):
        "helper function for sort()"
        new_string = ""
        for line in sorted_list:
            for field in line:
                new_string += self.field_separator + field
            new_string += self.field_separator
            new_string += self.line_separator
        return new_string

    def __merge(self, *args):
        """merge sorted files from args into one
           sorted file"""
        try:
            out = open(self.output_file, "w")
        except IOError:
            print "file does not exist"
            exit()
        tmp_str = str(unichr(127))
        args = list(args)[0]
        while True:
            for f in args:
                x = self.__readline(f)
                if x:
                    if x >= tmp_str:
                        continue
                    else:
                        ts = f
                        tmp_str = x
                else:
                    args.remove(f)
            if len(args) == 0:
                break
            if not tmp_str:
                break
            out.write(tmp_str)
            ts.seek(len(tmp_str), 1)
            tmp_str = str(unichr(127))
        out.close()
        return out

    def __readline(self, f):
        """returns line defined by self.line_separator
           without moving file pointer"""
        tmp = ""
        while True:
            x = f.read(1)
            if not x:
                tmp += x
                f.seek(-len(tmp), 1)
                return tmp
            tmp += x
            if x == self.line_separator:
                f.seek(-len(tmp), 1)
                return tmp

    def __check(self):
        try:
            with open(self.input_file) as infile:
                while True:
                    line = self.__readline(infile)
                    infile.seek(len(line), 1)
                    nextline = self.__readline(infile)
                    infile.seek(len(nextline), 1)
                    if not (line or nextline):
                        break
                    if line[:3] > nextline[:3]:
                        return False
                return True
        except IOError:
            print "bad input"
            return False
