# Класс доска
class Board:
    def __int__(self, hiden=False, size=6):
        # Скрытая доска, по умолчанию нет
        self.hiden = hiden
        # Размер доски, по умолчанию 6
        self.size = size
        # Создадим пустое поле

    def __str__(self):
        return f'Привет{self.size}'

if __name__ == '__main__':

    b = Board()
    print(b)
