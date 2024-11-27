#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Nov  3 18:17:27 2024

@author: vdzmshacu
"""

#Определение функции
def root_calculation(c_a, c_b, c_c):

    """
    Функция, которая определяет наличие корней у квадратного уравнения вида: a*x(^2)+b*x+c=0.
    Принимает на вход значения коэффициентов a, b, c квадратного уравнения.
    Показывает результат в виде значений корней квадратного уравнения либо сообщает, что корней нет. 
    """
    
    D = (c_b * c_b)-(4 * c_a * c_c);
    if D > 0:
        root_1 = (-c_b + (D ** (0.5))) / (2 * c_a);
        root_2 = (-c_b - (D ** (0.5))) / (2 * c_a);
        print(f"Квадратное уравнение имеет два корня: {root_1:.3f}, {root_2:.3f}");
    if D == 0:
        root_0 = (-c_b)/(2 * c_a);
        print(f"Квадратное уравнение имеет один корень кратности 2: {root_0:.3f}");
    if D < 0:
        print("Квадратное уравнение не имеет корней");
    return 0;

#Программа для нахождения корней квадратного уравнения

#Вывод начальных условий работы программы
print("Введите значения коэффициентов a, b, c квадратного уравнения вида: a*x(^2)+b*x+c=0");

#Ввод значений коэффициентов квадратного уравнения:
a = float(input("Введите значение коэффициента a: "));
b = float(input("Введите значение коэффициента b: "));
c = float(input("Введите значение коэффициента c: ")); 

#Вызов функции
root_calculation(a, b, c);  