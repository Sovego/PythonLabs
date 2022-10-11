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
