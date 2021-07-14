# #класс исключения
# #len - длина квадратной доски
# class Exclusion:
#     def __init__(self, x,y,len):
#         self.x = x
#         self.y = y
#         self.len = len
#     @out_coordinates.setter
#     #
#
#     #Декоратор проверки координат
#     def decorator_out_coordinates(self,coordinates):
#         def wrapper():
#             if coordinates <= len and coordinates >= 0:
#                 return coordinates
#             else BoardOutException('Неверные координаты'),
#
#     def

#Класс точек на поле
class Dot:
    def __init__(self, x, y):
        #координаты точки
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

    # Для сравнение точек
    # Для сравнение точек  и/или поиска в списке точек через in
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    # # Для вывода на экра координат точек
    # def __str__(self):
    #     return f' X:{self.x}, Y:{self.y}'

# Класс корабль
class Ship:
    def __init__(self, size,dotship,direction = False):
        #Длина корабля
        self.size = size
#        print(size)
        #Координаты носа корабль
        self.dotship = dotship
        #Направление корабля, по умолчанию вертикали, т.е. False
        self.direction = direction
        #Жизни
        self.health = size
        ## Массив координат корабля, к примеру Ship.dots() = [Dot,Dot,Dot]
        # self.shipdots = []


        #Возвращает список всех точек корабля
    def dots(self):
        # Заполнение по горизонтале или вертикале
        if self.direction:
            self.shipdots = [(Dot((self.dotship.x -1 ) + i,(self.dotship.y - 1 ))) for i in range(self.size)]
        else:
            self.shipdots = [(Dot((self.dotship.x - 1),(self.dotship.y -1 + i))) for i in range(self.size)]

        return self.shipdots

    # # def __str__(self):
    # #     return f'Ship: Размер: {self.size},Координаты носа:{self.dotship}, Направление корабля {self.direction }, жизни: {self.health}'
    # def __str__(self):
    #  return f'{self.shipdots}'

#Класс поле
class Board:
    def __init__(self):
        #Двумерный список, в котором хранятся состояния каждой из клеток.
        self.board_player = [['О' for i in range(6)] for j in range(6)]
        #Список кораблей на доске
        self.ships = []
        #Показывать ли поле, по умолчанию False
        self.hidden = False
        #Количество живых кораблей на доске.
        self.count_ive_ships = 0

    #Добавление корабля на доску
    def add_ship(self, addship):
        for i in range(len(addship)):

#            print(addship[i].x,addship[i].y)
            self.board_player[addship[i].x] [addship[i].y] = "■"
        pass



    # Печатаем поле
    def print_pole(self):
        print('    ', *range(1, len(self.board_player) + 1))
        for i in range(len(self.board_player)):
            print('', i + 1, '|', *self.board_player[i])






if __name__ == '__main__':
    p1=Dot(1,2)
    p2=Dot(1,2)
#    print_pole(Pole)
    Ship1=Ship(3,p1,True)
    Ship1.dots()
    Board1 = Board()
#    print(Board1.board_player)
    Board1.print_pole()
    Board1.add_ship(Ship1.shipdots)
    Board1.print_pole()



    # print(type(Ship1))
    # print(Ship1.shipdots)
    # print(type(Ship1.shipdots))
    # print(Ship1.size)
    # for i in range(len(Ship1.shipdots)):
    #     temp = Ship1.shipdots[i]
    #     print(temp.x,temp.y)
