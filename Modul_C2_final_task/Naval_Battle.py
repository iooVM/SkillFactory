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


class Ship:
    def __init__(self, size,count, x,y):
        self.size = size
        self.count = count
        self.x = x
        self.y = y
    def

class Board:
    def __init__(self, size, Player):


if __name__ == '__main__':
    print('hi')
