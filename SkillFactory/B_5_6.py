# Игрок, тип O или Х
USER = 'X'
# Длина оси Х
x = 3
# Длина оси У
y = 3
# Количество совпадений для победы
N = 3
# Генерируем поле
poleX0 = [['-' for j in range(x)] for i in range(y)]
# Есть ли в строке свобоное место
full_line = [False for j in range(x)]


# Печать поля
def print_poleX0(pole):
    print(' ', *range(x))
    for i in range(len(pole)):
        print(i, *pole[i])


# Заполняем поле
def imput_coordinates(poleX0loc, USERS, xx, yy):
    error = 0
    if xx > (len(poleX0loc) - 1) or yy > (len(poleX0loc[0]) - 1):
        error = 1
    elif poleX0loc[xx][yy] != '-':
        error = 2
    else:
        poleX0loc[xx][yy] = USERS
    return poleX0loc, error


# Условие победы
def if_win(poleX0loc, USER, N):
    # Развернём поле на 90 градусов
    rotate_poleX0loc = [[poleX0loc[j][i] for j in range(len(poleX0loc))] for i in range(len(poleX0loc[0]) - 1, -1, -1)]
    # Счётчик для проверки диагонали
    ii = 0
    # Буфера для проверки по диагонали
    # Проверку победы в одну линию
    for i in range(len(poleX0loc)):
        if (poleX0loc[i].count(USER) >= N) or (rotate_poleX0loc[i].count(USER) >= N):
            return True
    # Проверка по диагональ, порнуха конечно, но лучшего способа не придумал.
    # Если размер поля не 3 на 3, переделать
    if poleX0loc[ii][ii] == poleX0loc[ii + 1][ii + 1] == poleX0loc[ii + 2][ii + 2] == USER or poleX0loc[ii + 2][ii] == \
            poleX0loc[ii + 1][ii + 1] == poleX0loc[ii][ii + 2] == USER:
        return True
    return False


print_poleX0(poleX0)

while True:

    print(f' Ход {USER}')
    inx = input('Введите координаты по вертикали')
    if not inx.isdigit():
        print('ВВедены некоректные коодниаты ')
        continue
    iny = input('Введите координаты по горизонтали ')
    if not iny.isdigit():
        print('ВВедены некоректные коодниаты ')
        continue
    xx = int(inx)
    yy = int(iny)
    poleX0, error = imput_coordinates(poleX0, USER, xx, yy)
    if error:
        if error == 1:
            print('Неверные коодинаты')
            continue
        elif error == 2:
            print('Поле занято')
            continue
    print_poleX0(poleX0)
    # Проверка на свободные ячейки в поле
    for i in range(len(poleX0)):
        if '-' not in poleX0[i]:
            full_line[i] = True
        else:
            full_line[i] = False
    if False not in full_line:
        print('Мест нет. Гаме овер ')
        break
    if if_win(poleX0, USER, N):
        print(f'Победил {USER}')
        break

    # Смена пользователя
    if USER == 'X':
        USER = 'O'
    else:
        USER = 'X'
