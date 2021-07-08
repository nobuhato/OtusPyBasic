"""
Домашнее задание №1
Функции и структуры данных
"""


# def power_numbers(*args):
#     """
#     функция, которая принимает N целых чисел,
#     и возвращает список квадратов этих чисел
#     power_numbers(1, 2, 5, 7)
#     """
#     arr = [i**2 for i in args ]
#     print(arr)
#
# power_numbers(1,2,5,7)





# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(arr, tp):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if tp == ODD:
        l = filter(lambda x: x%2==1, arr)
        print(list(l))

    if tp == EVEN:
        l = filter(lambda x: x%2==0, arr)
        print(list(l))

    # if tp = PRIME:
    #     l =

filter_numbers([1, 2, 3], ODD)
filter_numbers([2, 3, 4, 5], EVEN)
# filter_numbers(, PRIME)
