from typing import Generator

# ЗАДАЧА 1
# O(n) - нужно пробежать по каждому элементу первого списка и проверить наличие его во втором
# поиск элемента во множестве О(1). Общая сложность алгоритма О(n)
# Затрачено памяти О(m). Выделена память под множество
def difference(first: list, second: list):
    return [i for i in first if i not in set(second)]


# O(n) - нужно пробежать по каждому элементу первого списка и проверить наличие его во втором
# поиск элемента во втором списке О(m). Общая сложность алгоритма О(n*m)
# Затрачено памяти О(1)
def difference(first: list, second: list):
    return [i for i in first if i not in second]


# ЗАДАЧА 2
array = [0, 1, 0, 0, 4, 5, 6, 7, 0, 8, -4]

# O(n) - сложность выполнения. каждый элемент списка обрабатывается единожды
# O(1) - памяти. ленивый генератор. Так же можно сделать генератор с yield
def clean_zero(array: list[int]) -> Generator[int, None, None]:
    return ([i for i in array if i != 0])
