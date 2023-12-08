import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Задание 1
Fun_x = []
x = 1.21
a = 3.5
while a <= 25.5:
    y = np.arcsin(x / 3) + 1.2 * a
    Fun_x.append(y)
    a += 1.5

a_values = np.arange(3.5, 26, 1.5)[:len(Fun_x)]  # Обрезаем a_values до длины Fun_x
Res = pd.DataFrame({"a": a_values, "f(a)": Fun_x})
print(Res)
print("Наибольшее значение - {}".format(max(Fun_x)))
print("Наименьшее значение - {}".format(min(Fun_x)))
print("Среднее значение - {}".format(np.mean(Fun_x)))
print("Количество элементов массива значений функции f(a) - {}".format(len(Fun_x)))
print("Отсортированный по убыванию numpy-массив f(a)")
print(np.sort(Fun_x, axis=None))

plt.plot(a_values, Fun_x, label="3.5<=a<=25.5; 5<f(a)<30")      #строит график
plt.axhline(y=np.mean(Fun_x), color="red", label="среднее значение функции f(a)")     #Добавляет горизонтальную линию на графике
plt.title("График изменения значений функции f(a)")
plt.xlabel("Значение аргумента а")    #Подписи осей
plt.ylabel("Значение функции f(a)")
plt.legend(loc="upper right", frameon=False)     #в правом верхнем углу без рамки
plt.show()

# Задание 2
u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]   #создаёт равномерные сетки  0-2П с шагом 20...
x = np.cos(u) * np.sin(v)
y = np.cos(v) * np.sin(u)
z1 = x ** 0.25 + y ** 0.25
z2 = x ** 2 - y ** 2
z3 = 2 * x + 3 * y
z4 = x ** 2 + y ** 2
z5 = 2 + 2 * x + 2 * y - x ** 2 - y ** 2

fig = plt.figure()      #отображение графиков
ax = fig.add_subplot(2, 2, 1, projection='3d')   #2x2 позиция 1, 3d
ax.plot_surface(x, y, z1)                   #построения трехмерных поверхностей на графике
ax = fig.add_subplot(2, 2, 2, projection='3d')
ax.plot_wireframe(x, y, z2)
ax = fig.add_subplot(2, 2, 3, projection='3d')
ax.plot_wireframe(x, y, z3)
ax = fig.add_subplot(2, 2, 4, projection='3d')
ax.scatter(x, y, z4)
ax = fig.add_subplot(2, 1, 1, projection='3d')
ax.plot_surface(x, y, z5)
plt.show()