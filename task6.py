import random

while True:
    try:
        quantity = int(input("Введте количество чисел в кортеже:"))
        if quantity<=0:
            print("Введите положительное число")
        else:
            break
    except ValueError:
        print("Ошибка ввода")

list_nums = [random.randint(-100, 100) for i in range(quantity)]
tuple_nums=tuple(list_nums)
print("Созданный кортеж чисел:",tuple_nums)

first_negative_index = None

for i, num in enumerate(tuple_nums):
    if num < 0:
        first_negative_index = i
        break  # Выходим из цикла после нахождения первого отрицательного числа

if first_negative_index is not None:
    print(f"\nИндекс первого отрицательного элемента: {first_negative_index}")
else:
    print("Отрицательные элементы отсутствуют в кортеже.")
