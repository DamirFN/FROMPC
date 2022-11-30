# # функцию, которая будет перемножать любое количество переданных ей аргументов.
# def add_func(*args):
#     prod = 1
#     for n in args:
#         prod = prod * n
#     return prod
# print(add_func(1, 3, 5, 5))
#
# # функцию, которая будет сумировать любое количество переданных ей аргументов.
# def adder(*nums):
#     sum_ = 0
#     for n in nums:
#         sum_ += n
#
#     return sum_
#
# print(adder(1, 2, 3))
#
# # А собственно *args — это кортеж, а **kwargs  — это словарь.
# def my_func(*args, **kwargs):
#    print(type(args))
#    print(type(kwargs))
#
# # Работа оператора звездочка для рапаковки списков или кортежей
# a = [1, 2, 3]
# b = [a, 4, 5, 6]
# print(b)
# # [[1, 2, 3], 4, 5, 6]
#
# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

