import operator

from commons import utils as ut


def info(o):
    class_strs = map(operator.attrgetter('__name__'), o.__class__.mro())
    supers = ' < '.join(ut.list_dedup(class_strs))

    ret = ut.StringBuilder()
    ret.write_line(supers)
    ret.nl()

    attrs = [x for x in dir(o) if not x.startswith('_')]

    def attr(x):
        try:
            return o.__getattribute__(x)
        except:
            return None

    funcs, attrs = ut.lsplit(attrs, lambda x: callable(attr(x)))

    funcs = [f + '()' for f in funcs]

    ret.write_line('\n'.join(attrs), indent=1)
    ret.nl()
    ret.write_line('\n'.join(funcs), indent=1)
    print(str(ret))