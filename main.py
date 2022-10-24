import numpy as np

# Задание 1
# Импортируйте библиотеку Numpy и дайте ей псевдоним np.
# Создайте массив Numpy под названием a размером 5x2, то есть состоящий из 5 строк и 2 столбцов. Первый столбец должен содержать числа 1, 2, 3, 3, 1, а второй - числа 6, 8, 11, 10, 7.
# Будем считать, что каждый столбец - это признак, а строка - наблюдение.
# Затем найдите среднее значение по каждому признаку, используя метод mean массива Numpy. Результат запишите в массив mean_a, в нем должно быть 2 элемента.

a = np.array([[1, 6],
              [2, 8],
              [3, 11],
              [3, 10],
              [1, 7]])

a_mean = a.mean(axis=0)

# Задание 2
# Вычислите массив a_centered, отняв от значений массива “а” средние значения соответствующих признаков, содержащиеся в массиве mean_a.
# Вычисление должно производиться в одно действие. Получившийся массив должен иметь размер 5x2.

a_centered = a - a_mean

# Задание 3
# Найдите скалярное произведение столбцов массива a_centered.
# В результате должна получиться величина a_centered_sp.
# Затем поделите a_centered_sp на N-1, где N - число наблюдений.

a_centered_sp = a_centered[0:6, 0] @ a_centered[0:6, 1]
a_centered_sp_1 = a_centered_sp / (a.shape[0] - 1)

# Задание 4**
# Число, которое мы получили в конце задания 3 является ковариацией двух признаков, содержащихся в массиве “а”.
# В задании 4 мы делили сумму произведений центрированных признаков на N-1, а не на N, поэтому полученная нами величина является несмещенной оценкой ковариации.
# В этом задании проверьте получившееся число, вычислив ковариацию еще одним способом - с помощью функции np.cov.
# В качестве аргумента m функция np.cov должна принимать транспонированный массив “a”. В получившейся ковариационной матрице (массив Numpy размером 2x2) искомое значение ковариации будет равно элементу в строке с индексом 0 и столбце с индексом 1.

m = np.cov(a.transpose())