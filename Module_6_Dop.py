class Figure:
    sides_count = 0

    def __init__(self,__color, __sides):
        self.__sides = [__sides]
        self.__color = __color
        self.filled = bool

        if len(*self.__sides) != self.sides_count:
            self.__sides = [1] * self.sides_count

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r: int, g: int, b: int):
        flag = False
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            flag = True
        if not flag:
            print("Ошибка в значении цвта")
        return flag

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        flag1 = False
        for i in args:
            if isinstance(i, int) and i > 0:
                flag1 = True
        if len(*args) == len(self.__sides) and flag1:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len([*new_sides]) == self.sides_count:
            self.__sides = [*new_sides]
        return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self,__color, *__sides):
        super().__init__(__color, __sides)
        self.__radius = None

    def get_radius(self):
        self.__radius = self.get_sides()[0]/6.28
        return self.__radius

    def get_square(self):
        return round(self.get_radius() ** 2 * 3.14, 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)

    def get_square(self):
        p = len(Triangle)/2
        square = (p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2])) ** 0.5
        return square

class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)
        self._sides = [__sides]
        if len(*self._sides) != self.sides_count/12:
            self._sides = [1] * self.sides_count

    def set_sides(self, *new_sides):
        if len([*new_sides]) == self.sides_count/12:
            self._sides = [*new_sides] * self.sides_count
        else:
            self._sides = [self.get_sides()] * self.sides_count
        return self._sides

    def get_sides(self):
        return self._sides

    def get_volume(self):
        return self.get_sides()[0] ** 3

circle1 = Circle((200, 200, 100), 10, 5)
print(circle1.get_sides())# (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
print(cube1.get_sides())
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
cube1.set_sides(5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
print(len(circle1))
# print(cube1.get_volume())
print(circle1.get_square())

# fig = Figure((222, 35, 130), 6)
# fg = fig.get_color()
# fig.set_color(25, 70, 100)
# print(fig.get_color())
# print(fig.get_sides())
# print(len(fig))
# print(fig.set_sides(7))
# print(type(fg))