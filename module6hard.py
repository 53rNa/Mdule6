# Задание "Они все так похожи"

class Figure:
    # Создаем атрибут класса
    sides_count = 0

    # При создании объектов делаем проверку на количество переданных сторон, если сторон не ровно sides_count,
    # то создаем массив с единичными сторонами и в том кол-ве, которое требует фигура:
    def __init__(self, color, sides, filled=False):
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        elif self.__is_valid_sides(*sides):
            self.__sides = sides
        if self.__is_valid_color(*color):
            self.__color = list(color)  # список цветов в формате RGB
        self.filled = filled  # закрашенный

    # Метод для проверки корректности цвета __is_valid_color - служебный, принимает параметры r, g, b, который
    # проверяет корректность переданных значений перед установкой нового цвета. Корректный цвет: все значения
    # r, g и b - целые числа в диапазоне от 0 до 255 (включительно):
    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in (r, g, b))

    # Метод для установки нового цвета set_color принимает параметры r, g, b - числа и изменяет атрибут __color на
    # соответствующие значения, предварительно проверив их на корректность. Если введены некорректные данные,
    # то цвет остаётся прежним.
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    # Метод get_color, возвращает список RGB цветов.
    def get_color(self):
        return self.__color

    # Метод для проверки сторон__is_valid_sides - служебный, принимает неограниченное кол-во сторон,
    # возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с
    # текущим (sides_count), False - во всех остальных случаях.

    def __is_valid_sides(self, *new_sides):
        # return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

        # Проверка, что количество переданных сторон совпадает с sides_count
        if len(new_sides) != self.sides_count:
            return False

        # Проверка, что все стороны являются положительными целыми числами
        for side in new_sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    # Метод get_sides возвращает значениея атрибута __sides.
    def get_sides(self):
        return self.__sides

    # Метод для установки новых сторон
    # Метод set_sides(self, *new_sides) принимает новые стороны, если их количество не равно sides_count, то
    # не изменять, в противном случае - менять.
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    # Метод для вычисления периметра (сумма всех сторон)
    # __len__ возвращает периметр фигуры.
    def __len__(self):
        return sum(self.__sides)

# Класс Circle
class Circle(Figure):
    sides_count = 1

    def __init__(self, color, round, filled=False):
        super().__init__(color, [round], filled)

        # Радиус рассчитывается исходя из длины окружности (одной единственной стороны):
        self.__radius = round / (2 * 3.14159)

    def get_radius(self):
        return self.__radius  # возвращает значение радиуса

    def get_square(self):
        return 3.14159 * self.__radius ** 2  # возвращает площадь круга


# Класс Triangle
class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides, filled=False):
        super().__init__(color, [sides]*1, filled)
        self.__height = self.get_height()

    # Метод get_height возвращает высоту треугольника:
    def get_height(self):
        # Формула Герона для нахождения площади треугольника
        # Если в условии даны длины трех сторон треугольника, то площадь треуголника по формуле Герона:
        # S = (p*(p-a)*(p-b)*(p-c))^1/2, где p – полупериметр треугольника; а, b, с – его стороны.
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        # Вычисление высоты треугольника относительно его стороны a:
        height = (2 * S) / a
        return height

    # def get_height(self):
    #     return self.__height

    # Метод get_square возвращает площадь треугольника:
    def get_square(self):
        a, b, c = self.get_sides()
        return 0.5 * a * self.__height

# Класс Cube
class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length, filled=False):
        # Переопределяем __sides сделав список из 12 одинаковых сторон (передаётся 1 сторона)
        super().__init__(color, [side_length] * 12, filled)

    def get_volume(self):
        # Вычисляем объем куба
        side_length = self.get_sides()[0]
        return side_length ** 3

circle1 = Circle((200, 200, 100), 10, 15)  # (Цвет, стороны)
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
