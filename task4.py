import random
while True:
    try:
        quantity = int(input("Введте количество чисел в последовательности:"))
        if quantity<=0:
            print("Введите положительное число")
        else:
            break
    except ValueError:
        print("Ошибка ввода")
sequence = [random.randint(0, 9) for i in range(quantity)]  # Пример случайной последовательности чисел
print("\nСлучайная последовательность чисел:",sequence)
# Создаем пустой словарь
number_count = {}

# Перебираем каждый символ в последовательности
for char in sequence:
    number = int(char)  # Приводим символ к типу int
    if number in number_count:
        number_count[number] += 1  # Увеличиваем счетчик числа, если оно уже есть в словаре
    else:
        number_count[number] = 1  # Добавляем число в словарь со значением 1, если оно встречается первый раз

# Выводим словарь с количеством чисел
print("\nСловарь, созданный на основе последовательности:",number_count)
