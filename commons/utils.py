import textwrap


def list_dedup(l):
    seen = set()
    result = []
    for item in l:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def lsplit(list, predicate):
    l1 = []
    l2 = []
    for i in list:
        if predicate(i):
            l1.append(i)
        else:
            l2.append(i)
    return l1, l2


class StringBuilder:

    def __init__(self):
        self.s = ''

    def nl(self):
        self.s += '\n'

    def write(self, txt, indent=0):
        if indent > 0:
            self.s += textwrap.indent(txt, '\t')
        else:
            self.s += txt

    def write_line(self, txt, indent=0):
        self.write(txt, indent)
        self.nl()

    def write_list(self, txt_list, indent=0):
        self.write_line('\n'.join(txt_list), indent)

    def __str__(self):
        return self.s

    def __repr__(self):
        return self.s