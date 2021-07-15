try:
    age = int(input("Сколько тебе лет?"))

    if age > 100 or age <= 0:
        raise ValueError("Тебе не может быть столько лет")

    # Возраст выводится только если пользователь ввёл правильный возраст.
    print(f"Тебе {age} лет!")
except ValueError:
    print("Неправильный возраст")


