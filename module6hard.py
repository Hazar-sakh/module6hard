class Figure:
    sides_count = 0

    def __init__(self, __color: list, __sides: list, filled=bool):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            color_valid = True
            return color_valid


    def set_color(self, r, g, b):
        color_V = self.__is_valid_color(r, g, b)
        if color_V:
            self.__color = r, g, b
            return self.__color


    def __is_valid_sides(self, sides):
        for i in sides:
            if isinstance(i, int) and i == self.__sides:
                sides_valid = True
                return sides_valid
            else:
                sides_valid = False
                return sides_valid

    def get_sides(self):
        return self.__sides

    def __len__(self):
        perimetr = 0
        for i in self.__sides:
            perimetr += i
        return perimetr

    def set_sides(self, *new_sides):
        new_sides = list(new_sides)
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, __sides, filled=bool):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled
        super().__init__(__color, __sides, filled)
        self.__radius = __sides / (2 * 3.14)

    def get_square(self):
        square = 3.14 * (self.__radius ** 2)
        return square


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, __sides, filled=bool):
        super().__init__(__color, __sides, filled)
        self.__sides = __sides
        self.__color = __color
        self.filled = filled
        self.a = self.__sides[0]
        self.b = self.__sides[1]
        self.c = self.__sides[2]
        self.half_per = (self.a + self.b + self.c) / 2
        self.__height = ((self.half_per * (self.half_per - self.a) *
                          (self.half_per - self.b) * (self.half_per - self.c)) ** 0.5) * 2 / 3

    def get_square(self):
        square = (self.half_per * (self.half_per - self.a) *
                  (self.half_per - self.b) * (self.half_per - self.c)) ** 0.5
        return square


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, __sides, filled=bool):
        self.LiSides = [0]
        for i in self.LiSides:
            if len(self.LiSides) > self.sides_count:
                pass
            else:
                self.LiSides.append(__sides)
        self.LiSides.remove(0)
        __sides = self.LiSides
        self.side = self.LiSides[0]
        self.__color = __color
        self.filled = filled
        self.LiSides = [0]
        super().__init__(__color, __sides, filled)

    def get_volume(self):
        volume = self.side ** 3
        return volume


if __name__ in '__main__':

    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())
