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
        # self.shipdots = []


        #Возвращает список всех точек корабля
    def dots(self):
        # Заполнение по горизонтале или вертикале
        if self.direction:
            self.shipdots = [(Dot(self.dotship.x + i,self.dotship.y)) for i in range(self.size)]
        else:
            self.shipdots = [(Dot(self.dotship.x,self.dotship.y + i)) for i in range(self.size)]

        return self.shipdots

    # # def __str__(self):
    # #     return f'Ship: Размер: {self.size},Координаты носа:{self.dotship}, Направление корабля {self.direction }, жизни: {self.health}'
    # def __str__(self):
    #  return f'{self.shipdots}'

# Печатаем поле
def print_pole(pole):
    print('    ', *range(1,len(pole)+1))
    for i in range(len(pole)):
        print('',i+1,'|', *pole[i])



if __name__ == '__main__':
    p1=Dot(1,2)
    p2=Dot(1,2)
    print_pole(Pole)
    Ship1=Ship(5,p1,True)
    Ship1.dots()
    print(type(Ship1))
    print(Ship1.shipdots)
    print(type(Ship1.shipdots))
    print(Ship1.size)
    for i in range(len(Ship1.shipdots)):
        temp = Ship1.shipdots[i]
        print(temp.x,temp.y)
