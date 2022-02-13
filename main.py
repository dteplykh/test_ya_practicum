from typing import Generator

# ЗАДАЧА 1
# O(n) - нужно пробежать по каждому элементу первого списка и проверить наличие его во втором
# поиск элемента во множестве О(1). Общая сложность алгоритма О(n)
# Затрачено памяти О(n+m). Выделена память под множество и результат
def difference(first: list, second: list):
    result = [i for i in first if i not in set(second)]


# O(n) - нужно пробежать по каждому элементу первого списка и проверить наличие его во втором
# поиск элемента во втором списке О(m). Общая сложность алгоритма О(n*m)
# Затрачено памяти О(n+m). Выделена память под результат
def difference(first: list, second: list):
    result = [i for i in first if i not in second]


# ЗАДАЧА 2
array = [0, 1, 0, 0, 4, 5, 6, 7, 0, 8, -4]

# O(n) - сложность выполнения. каждый элемент списка обрабатывается единожды
# O(1) - памяти.
def clean_zero(array: list[int]) -> list[int]:
    i = len(array) - 1
    while i >= 0:
        if array[i] == 0:
            array.pop(i)
        i-=1
    return array
