class Item:
    def __init__(self, count=3, max_count=16):
        self._count = count
        self._max_count = 16

    def update_count(self, val):
        if val <= self._max_count:
            self._count = val
            return True
        else:
            return False

    # Свойство объекта. Не принимает параметров кроме self, вызывается без круглых скобок
    # Определяется с помощью декоратора property
    @property
    def count(self):
        return self._count

    def __add__(self, num):
        """ Сложение с числом """
        return self.count + num

    def __mul__(self, num):
        """ Умножение на число """
        return self.count * num

    def __lt__(self, num):
        """ Сравнение меньше """
        return self.count < num

    def __eq__(self, num):
        return self.count == num

    def __ne__(self, num):
        return self.count != num

    def __gt__(self, num):
        return self.count > num

    def __le__(self, other):
        return self.count <= other

    def __ge__(self, other):
        return self.count >= other

    def __len__(self):
        """ Получение длины объекта """
        return self.count

    def __iadd__(self, other):
        a = self.count
        a += other
        return self.update_count(a)

    def __isub__(self, other):
        a = self.count
        a -= other
        return self.update_count(a)

    def __imul__(self, other):
        a = self.count
        a *= other
        return self.update_count(a)


class Apple(Item):
    def __init__(self, count=1, max_count=32, saturation=10):
        super().__init__(count, max_count)
        self._saturation = saturation


class Melon(Item):
    def __init__(self, count=1, max_count=32, saturation=20):
        super().__init__(count, max_count)
        self._saturation = saturation


class Bread(Item):
    def __init__(self, count=1, max_count=32, saturation=5):
        super().__init__(count, max_count)
        self._saturation = saturation


class Meat(Item):
    def __init__(self, count=1, max_count=32, saturation=50):
        super().__init__(count, max_count)
        self._saturation = saturation


class Inventory:
    def __init__(self, length=10):
        self._list = [None for _ in range(10)]

    def __getitem__(self, index):
        if index > len(self._list):
            raise IndexError(f'Index {index} more then {len(self._list)}')
        return self._list[index]

    def __setitem__(self, index, item):
        if index > len(self._list):
            raise IndexError(f'Index {index} more then {len(self._list)}')
        self._list[index] = item
        return self

    def takeitem(self, index, count):
        if index > len(self._list):
            raise IndexError(f'Index {index} more then {len(self._list)}')
        if self._list[index].Item < count:
            raise Exception(f'Count {count} more then {self._list[index].Item.count}')
        self._list[index].Item -= count
        if self._list[index].Item == 0:
            self._list[index] = None


class Deque:
    def __init__(self):
        self._deque = []

    def __getitem__(self):
        return self._deque.pop(0)

    def __setitem__(self, value):
        self._deque.append(value)

    @property
    def get_list(self):
        return self._deque.copy
