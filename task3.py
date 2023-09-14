import random

try:
    numbers = [random.randint(1, 100) for i in range(30)]  # Генерируем список случайных чисел от 1 до 10
    print("Список чисел:", numbers)

    pairs = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                pairs += 1
                print("Числа, равные друг другу:", numbers[i])

    print("\nКоличество пар элементов, равных друг другу:", pairs)

except Exception as e:
    print("Произошла ошибка:", e)

