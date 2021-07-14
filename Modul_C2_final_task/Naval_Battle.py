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

# Нарисуем ручками поле
Pole = [[ 'О','О','О','О','О','О'],
 ['О','О','О','О','О','О'],
 ['О','О','О','О','О','О'],
 ['О','О','О','О','О','О'],
 ['О','О','О','О','О','О'],
 ['О','О','О','О','О','О']]


#Класс точек на поле
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

    # Для сравнение точек
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    def __str__(self):
        return f' X:{self.x}, Y:{self.y}'

# Класс корабль
class Ship:
    def __init__(self, size,dotship,direction = True):
        #Длина корабля
        self.size = size
#        print(size)
        #Координаты носа корабль
        self.dotship = dotship
        #Направление корабля, по умолчанию горизонталь, т.е. True
        self.direction = direction
        #Жизни
        self.health = size
        ## Массив координат корабля, к примеру Ship.dots() = [Dot,Dot,Dot]
        self.shipdots = []


        #Возвращает список всех точек корабля
    def dots(self):

        if self.size > 1:
            pass
        else:
#            print(self.dotship)
            self.shipdots.append(self.dotship)
#            print(self.shipdots)
            return self.shipdots

        # if size:
        #     if direction dotship
        # return shipdots
        #  По умолчанию по горизонтали

        pass


    def __str__(self):
        return f'Ship: Размер: {self.size},Координаты носа:{self.dotship}, Направление корабля {self.direction }, жизни: {self.health}'

def print_pole(pole):
    print('    ', *range(1,len(pole)+1))
    for i in range(len(pole)):
        print('',i+1,'|', *pole[i])



if __name__ == '__main__':
    p1=Dot(1,2)
    p2=Dot(1,2)
    # print(p1==p2)
    # print(str(p1))
    # print(p2)
    print_pole(Pole)
    # print(p1.x)
    # print(p1.y)
    Ship1=Ship(1,p1,True)
    #print(type(Ship1.dots()))
    print(Ship1)
    Ship1Dots = Ship1.dots()
#    print(Ship1Dots)
    # for i in Ship1Dots:
    #     print('1',i)

# print(Pole)
# print('test')

