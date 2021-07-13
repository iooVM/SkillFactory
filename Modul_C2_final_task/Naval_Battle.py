#класс исключения
#len - длина квадратной доски
class Exclusion:
    def __init__(self, x,y,len):
        self.x = x
        self.y = y
        self.len = len
    @out_coordinates.setter
    #

    #Декоратор проверки координат
    def decorator_out_coordinates(self,coordinates):
        def wrapper():
            if coordinates <= len and coordinates >= 0:
                return coordinates
            else BoardOutException('Неверные координаты'),

# Класс корабль
class Ship:
    def __init__(self, size,dotship,direction,health):
        #Длина корабля
        self.size = size
        #Координаты носа корабль
        self.dotship = dotship
        #Направление корабля
        self.direction = direction
        #Жизни
        self.health = health
    #Возвращает список всех точек корабля
    def dots(self):

    def
#класс доска
class Board:
    def __init__(self, size):
        poleX0 = [['-' for j in range(x)] for i in range(y)]
        self.size = size
class Dot:
    def __init__(self, size, Player):
        self.x = x
        self.y = y


if __name__ == '__main__':
    print('hi')
