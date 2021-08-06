#импорт генератора случайных целых чисел
from random import randint

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
        #Число ходов
        self.count = 0

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
        #Рисуем корабль
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
        #Добавляем точку в список занятых
        self.busy.append(d)

        #Проверка на попадание
        for ship in self.ships:
            # Если попдание в корабль
            if d in ship.dots:
                # Отнимаем жизнь
                ship.health -= 1
                self.pole[d.x][d.y] = "X"
                # Если корабль унечтожен
                if ship.health == 0:
                    self.count += 1
                    self.contour(ship, verb = True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True
        self.pole[d.x][d.y] = "."
        print("Мимо!")
        return False
    #Начало игры с пустой доской
    def begin(self):
        self.busy = []

# класс игрока
class Player:
    def __init__(self, board, enemy):
        #Доска игрока
        self.board = board
        #Кто играет
        self.enemy = enemy
    # Пустой метод для потомков класса, запрос на выстрел
    def ask(self):
        raise NotImplementedError()
    #
    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)

# Дочерний класс для ИИ
class AI(Player):
    def ask(self):
        # Случайный выстрел в клетку
        d = Dot(randint(0, 5), randint(0, 5))
        print(f"Ход компьютера: {d.x + 1} {d.y + 1}")
        return d

# Дочерний класс Игрока ( человека из консоли)
class User(Player):
    # Запрос на выстрел
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:
                print(" Введите 2 координаты! ")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Введите числа! ")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)

#Класс игра
class Game:
    def __init__(self, size=6):
        #Размер доски
        self.size = size
        #Генерируем доску пользователя в случайном порядке, т.к. на проверке лениво самому расставлять
        pl = self.random_board()
        # Генерируем скрытую доску ИИ
        co = self.random_board()
        co.hid = True

        # Экземпляры досок игрока и ИИ
        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def try_board(self):
        #Какие корабли и сколько
        lens = [3, 2, 2, 1, 1, 1, 1]
        #Рисуем доску
        board = Board(size=self.size)
        # Счётчик попыток случайного располежения кораблей
        attempts = 0
        # расположение кораблей

        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                # случайное рассположение корабля
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))
                # попытка раместить корабль на доску
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board
    #Генерим поле кораблей, если не получилось, пробуем ещё раз
    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    #Приветствие перед началом игры
    def greet(self):
        print("-------------------")
        print("  Приветсвуем вас  ")
        print("      в игре       ")
        print("    морской бой    ")
        print("-------------------")
        print(" формат ввода: x y ")
        print(" x - номер строки  ")
        print(" y - номер столбца ")
    # Цикл игры
    def loop(self):
        # Номер хода
        num = 0
        # Интерфейс игры
        while True:
            print("-" * 20)
            print("Доска пользователя:")
            print(self.us.board)
            print("-" * 20)
            print("Доска компьютера:")
            print(self.ai.board)
            print("-" * 20)
            if num % 2 == 0:
                print("Ходит пользователь!")
                repeat = self.us.move()
            else:
                print("Ходит компьютер!")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.count == 7:
                print("-" * 20)
                print("Пользователь выиграл!")
                break

            if self.us.board.count == 7:
                print("-" * 20)
                print("Компьютер выиграл!")
                break
            num += 1
    # Метод для запуска игры
    def start(self):
        self.greet()
        self.loop()

if __name__ == '__main__':
    # # p1=Dot(1,2)
    # # p2=Dot(1,2)
    # # print(p1==p2)
    # # print(str(p1))
    # # print(p2)
    # # # print_pole(Pole)
    # # #Тестовый кораблик
    # # ship_test = Ship(p1, 3, False)
    # # print(ship_test.dots())
    # # print(ship_test.hited(Dot(0, 3)))
    # b = Board()
    # print(b)
    # Играем
    g = Game()
    g.start()
# print(Pole)
# print('test')
#test
#test2