# Pole = [ ['О'],['О'],['О'],['О'],['О'],['О'],
#  ['О'],['О'],['О'],['О'],['О'],['О'],
#  ['О'],['О'],['О'],['О'],['О'],['О'],
#  ['О'],['О'],['О'],['О'],['О'],['О'],
#  ['О'],['О'],['О'],['О'],['О'],['О'],
#  ['О'],['О'],['О'],['О'],['О'],['О']]
# Пустое поле
# Pole = [[ 'О','О','О','О','О','О'],
#  ['О','О','О','О','О','О'],
#  ['О','О','О','О','О','О'],
#  ['О','О','О','О','О','О'],
#  ['О','О','О','О','О','О'],
#  ['О','О','О','О','О','О']]


# Класс точка
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # # Геттер и сеттер для Х
    # def get_x(self,x):
    #     return self.x
    # def set_x(self, x):
    #     if  ((x > 0) and isinstance(x, int)):
    #         self.x = x
    #
    # # Геттер и сеттер для Y
    # def get_y(self,y):
    #     return self.y
    # def set_y(self, y):
    #     if  ((y > 0) and isinstance(y, int)):
    #         self.y = y

    # Переопределим параметр равенства точек
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Переопределим вывод точки , для корректного отображение содержимого, а не адресов на содержимое, используем __repr__
    def __repr__(self):
        return f'Dot{self.x, self.y}'


# Класс исключений
class BoardException(Exception):
    pass


# Исключение при попадании сне доски
class BoardOutException(BoardException):
    def __str__(self):
        return 'внедоски '


# Исключение при повторном выстреле
class BoardUsedException(BoardException):
    def __str__(self):
        return "повторный выстрел"


# Исключение при невозможности размещения корабля
class BoardWrongShipException(BoardException):
    pass


# Класс корабль
class Ship:
    def __init__(self, dotship, size, direction=True, ):

        # Координаты носа корабль
        self.dotship = dotship
        # Длина корабля
        self.size = size
        # Направление корабля, по умолчанию горизонталь, т.е. True
        self.direction = direction
        # Жизни
        self.health = size

    # Координаты точек корабля
    #    @property
    def dots(self):
        # Массив координат корабля, к примеру Ship.dots() = [Dot,Dot,Dot]
        shipdots = []
        # Возвращает список всех точек корабля
        for i in range(self.size):
            # Буферные параметры точек, для записи в список точек корабля
            dot_x = self.dotship.x
            dot_y = self.dotship.y

            # Если корабль горизонтальный, наращиваем X, иначе Y
            if self.direction:
                dot_x += i
            else:
                dot_y += i
            # Добавление точки в список точек корабля
            shipdots.append(Dot(dot_x, dot_y))
        return shipdots

    # Проверка на попадание в корабль
    def hited(self, hit):
        return hit in self.dots()


# def print_pole(pole):
#     print(' ', *range(len(pole)))
#     for i in range(len(pole)):
#         print(i+1, *pole[i])

# Класс доска
class Board:
    def __init__(self, hiden=False, size=6):
        # Скрытая доска, по умолчанию нет
        self.hiden = hiden
        # Размер доски, по умолчанию 6
        self.size = size
        # Создадим пустое поле
        self.pole = [['0'] * size for i in range(size)]
        #   self.field = [ ["O"]*size for _ in range(size) ]
        # Занятые клетки
        self.busy = []
        # Корабли
        self.ships = []

    # def __str__(self):
    #     return f'{self.pole}'
    # Вывод поля в print
    def __str__(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.pole):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"
        # Отображение поля в зависимоти от игрока
        if self.hiden:
            res = res.replace("■", "O")
        return res

    # Обводка точки
    def contour(self, ship, verb=False):
        # Добавляем занятые точки в список занятых точек
        neighbour = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        for d in ship.dots:
            for dx, dy in neighbour:
                cur = Dot(d.x + dx, d.y + dy)
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.pole[cur.x][cur.y] = "."
                    self.busy.append(cur)

    # проверка на попадание в доску
    def out(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))
    # добавление корадля на доску
    def add_ship(self, ship):
        for d in ship.dots:
            # Если точка занята, выдаём исключение
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()

        for d in ship.dots:
            self.pole[d.x][d.y] = "■"
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)
    #Стреляем
    def shot(self, d):
        #Если вне доски выдём исключение внедоски
        if self.out(d):
            raise BoardOutException()
        # Если клетка занята Исключение при повторном выстреле
        if d in self.busy:
            raise BoardUsedException()

if __name__ == '__main__':
    # p1=Dot(1,2)
    # p2=Dot(1,2)
    # print(p1==p2)
    # print(str(p1))
    # print(p2)
    # # print_pole(Pole)
    # #Тестовый кораблик
    # ship_test = Ship(p1, 3, False)
    # print(ship_test.dots())
    # print(ship_test.hited(Dot(0, 3)))
    b = Board()
    print(b)

# print(Pole)
# print('test')
#test
#test2