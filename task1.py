while True:
    while True:
        try:
            start = int(input("\nВведте начальное значение диапозона:"))
            break
        except ValueError:
            print("Ошибка ввода")
    while True:
        try:
            end = int(input("Введте конечное значение диапозона:"))
            break
        except ValueError:
            print("Ошибка ввода")
    if start==end:
        print("Введите два разных значения")
    elif start>end:
        print("Введите конечное значение больше начального")
    else: break
print("\nПростые числа в заданном диапазоне:")
count=0
for num in range(start, end+1):
    if num>1:
       for i in range(2,num):
           if (num%i)==0:
               break
       else:
           print(num)
           count +=1
if count==0:
    print("В данном диапазоне нет простых чисел")
