class PropCreator(type):
    def __new__(cls, name, base, d):
        prop = {}

        for name, obj in d.items():
            if not callable(obj):
                continue

            if name.startswith('get_'):
                prop.setdefault(name[4:], {})['fget'] = obj
            if name.startswith('set_'):
                prop.setdefault(name[4:], {})['fset'] = obj
            if name.startswith('del_'):
                prop.setdefault(name[4:], {})['fdel'] = obj

        for name, descriptors in prop.items():
            d[name] = property(**descriptors)
        return super().__new__(cls, name, base, d)


class Example(metaclass=PropCreator):
    def __init__(self):
        self._x = None

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return 'y'


if __name__ == '__main__':
    ex = Example()
    ex.x = 255
    print(ex.x)
    print(ex.y)
