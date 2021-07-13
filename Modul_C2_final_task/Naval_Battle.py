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
# #класс доска
# class Board:
#     def __init__(self, size):
#         poleX0 = [['-' for j in range(x)] for i in range(y)]
#         self.size = size

# Pole = [ ['О'],['О'],['О'],['О'],['О'],['О'],
#  ['О'],['О'],['О'],['О'],['О'],['О'],
#  ['О'],['О'],['О'],['О'],['О'],['О'],
#  ['О'],['О'],['О'],['О'],['О'],['О'],
#  ['О'],['О'],['О'],['О'],['О'],['О'],
#  ['О'],['О'],['О'],['О'],['О'],['О']]

Pole = [[ 'О','О','О','О','О','О'],
 ['О','О','О','О','О','О'],
 ['О','О','О','О','О','О'],
 ['О','О','О','О','О','О'],
 ['О','О','О','О','О','О'],
 ['О','О','О','О','О','О']]



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


    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    def __str__(self):
        return f'Dot: {self.x,self.y}'

# Класс корабль
class Ship:
    def __init__(self, size,dotship,health,direction = True,):
        #Длина корабля
        self.size = size
        #Координаты носа корабль
        self.dotship = dotship
        #Направление корабля, по умолчанию горизонталь, т.е. True
        self.direction = direction
        #Жизни
        self.health = health
    #Возвращает список всех точек корабля
    def dots(self):
        # Массив координат корабля, к примеру Ship.dots() = [Dot,Dot,Dot]
        shipdots = []
        return shipdots
        #  По умолчанию по горизонтали

def print_pole(pole):
    print(' ', *range(len(pole)))
    for i in range(len(pole)):
        print(i+1, *pole[i])



if __name__ == '__main__':
    p1=Dot(1,2)
    p2=Dot(1,2)
    print(p1==p2)
    print(str(p1))
    print(p2)
    print('test')
    print_pole(Pole)


# print(Pole)
# print('test')

