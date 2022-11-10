#!/usr/bin/env python3
# coding=utf-8

# Имеется двумерный массив 4x5. Реализовать возможность заполнения его
# случайными числами. Реализовать команду выполнить задание, которая выполняет:
# Если во втором столбце стоят две единицы, то уменьшить макс. элемент первой
# строки в два раза, а все единицы в таблице заменить нулями.
import re

import numpy as np
import random  # импортируем модуль random для генерации случайных чисел


# Функция генерирует nxm массив случайных чисел до max_value, у которого
# стандартное значение 20
import numpy as np

random_float_array = np.random.uniform(0, 100, size=(4, 5)) # Создаю рандом вещественного массива с помощью numpy, указаываю кол-во строк


""""
def print_array(random_float_array):  # функция выводит массив в удобочитаемой форме
    print()  # переход на новую строку
    # Циклу for также можно давать массивы, тогда перебирается каждый элемент
    for i in random_float_array:
        # Так как массив состоит из подмассивов, тогда каждый элемент тоже
        # можно перебрать используя цикл for
        for j in i:
            print("" , end='')  # выводим к1аждое значение и табуляцию
        print()  # переход на новую строку
"""

def main():

    random_float_array = np.random.uniform(0, 100, size=(4, 5)) # Создаю рандом вещественного массива с помощью numpy, указаываю кол-во строк
    random_float_array = np.around(random_float_array,2)
    print(re.sub('[\[\]]', '', np.array_str(random_float_array))) # Вывожу массив в удобной читаемой форме без скобок
    # Бесконечный цикл while, который закончится только при помощи break
    while True:
        print  # переход на новую строку
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание;")
        print("3. Выход.")
        # Получаем ввод команды от пользователя
        key = input('Введите команду (1, 2 или 3): ')
        if key == '1':  # если команда 1, то заполняем массив заново
            random_float_array = np.random.uniform(0, 100, size=(4, 5)) # Создаю рандом вещественного массива с помощью numpy, указаываю кол-во строк
            random_float_array = np.around(random_float_array, 2)
            print(re.sub('[\[\]]', '', np.array_str(random_float_array))) # Вывожу массив в удобной читаемой форме без скобок
            # После этого условия цикл начнется с начала
        elif key == '2':  # если команда 2, то проверяем условие
            print()  # переход на новую строку
            one_count = 0  # переменая для подсчета единиц во втором столбце

            if (random_float_array == 0 ).any():  # Проверяю наличие 0 в Массиве, так как значения float, то чистый 0 получить очень сложно
                                                #
                one_count += 1                  # Пользуемся any,который в nuppy служет булевым значением и определяет истина или ложь

            if one_count == 0:
                print("Нет 0 в Массиве")
                print("Задание не будет выполнено")
            else:
                print("0 найден в матрице")
                print("Все вещественные элементы заменены на 1")
                random_float_array = np.where(random_float_array <= 0, 1, 1)  # Пользуемся np.where, который  меняет вещ значения на 1
                random_float_array = np.around(random_float_array, 2)
                print(re.sub('[\[\]]', '', np.array_str(random_float_array)))  # Выводим Массив в удобной форме












        elif key == '3':
            exit(0)  # выходим из программы


if __name__ == '__main__':
    main()
