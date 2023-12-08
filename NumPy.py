import numpy as np

a=1.21
b=0.371
f1=np.array([np.tan(a+b)**2])
f2=np.array([-(a+1.5)**(1/3)])
f3=np.array([a*b**5])
f4=np.array([-(b/np.log(a**2))])
result=f1+f2+f3+f4
print("Задание 1.1:")
print(result)

X_column1=np.ones((12,1))     #Столбец из 1(12 строк,1 столбец)
X_column2=np.random.randint(17,29,(12,1))
X_column3=np.random.randint(60,82,(12,1))
X=np.hstack((X_column1,X_column2,X_column3))   #Объединение столбцов
Y=np.random.uniform(13.5,18.6,(12,1))   #uniform-чисел из равномерного распределения в указанном интервале

A=np.linalg.inv((np.transpose(X).dot(X))).dot(np.transpose(X).dot(Y))   #модуля numpy.linalg, inv()-обратная  dot()-умножение
print("\nЗадание 1.2:")
print(A)
