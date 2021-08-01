
# Pole = [ ['О'],['О'],['О'],['О'],['О'],['О'],
#  ['О'],['О'],['О'],['О'],['О'],['О'],
#  ['О'],['О'],['О'],['О'],['О'],['О'],
#  ['О'],['О'],['О'],['О'],['О'],['О'],
#  ['О'],['О'],['О'],['О'],['О'],['О'],
#  ['О'],['О'],['О'],['О'],['О'],['О']]
#Пустое поле
Pole = [[ 'О','О','О','О','О','О'],
 ['О','О','О','О','О','О'],
 ['О','О','О','О','О','О'],
 ['О','О','О','О','О','О'],
 ['О','О','О','О','О','О'],
 ['О','О','О','О','О','О']]


#Класс точка
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

    #Переопределим параметр равенства точек
    def __eq__(self,other):
            return self.x==other.x and self.y==other.y
    #Переопределим вывод точки , для корректного отображение содержимого, а не адресов на содержимое, используем __repr__
    def __repr__(self):
        return f'Dot: {self.x,self.y}'


#Класс исключений
class BoardException(Exception):
    pass
#Исключение при попадании сне доски
class BoardOutException(BoardException):
    def __str__(self):
        return 'внедоски '
#Исключение при повторном выстреле
class BoardUsedException(BoardException):
    def __str__(self):
        return "повторный выстрел"
#Исключение при невозможности размещения корабля
class BoardWrongShipException(BoardException):
    pass

# Класс корабль
class Ship:
    def __init__(self, dotship,size,direction = True,):

        #Координаты носа корабль
        self.dotship = dotship
        # Длина корабля
        self.size = size
        #Направление корабля, по умолчанию горизонталь, т.е. True
        self.direction = direction
        #Жизни
        self.health = size

    def dots(self):
        # Массив координат корабля, к примеру Ship.dots() = [Dot,Dot,Dot]
        shipdots = []
        # Возвращает список всех точек корабля
        for i in range(self.size):
            #Буферные параметры точек, для записи в список точек корабля
            dot_x = self.dotship.x
            dot_y = self.dotship.y

            # Если корабль горизонтальный, наращиваем X, иначе Y
            if self.direction:
                dot_x += i
            else:
                dot_y += i
            #Добавление точки в список точек корабля
            shipdots.append(Dot(dot_x,dot_y))
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
    #Тестовый кораблик
    ship_test = Ship(p1, 3, False)
    print(ship_test.dots())


# print(Pole)
# print('test')

