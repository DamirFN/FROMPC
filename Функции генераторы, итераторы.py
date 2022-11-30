
def fib():
    a, b = 0, 1
    yield a
    yield b

    while True:
         a, b = b, a + b
         yield b

for i in fib():     #Выведение новую пару последовательности Фибоначи имея только два первых значения
    print(i)


# Создать функцию-генератор, возвращающую бесконечную последовательность натуральных чисел. По умолчанию она начинается
# с единицы, её шаг равен 1, но пользователь может указать любой шаг и любое число в качестве аргумента функции, с
# которого будет начинаться последовательность.
# def count(start=1, step=1):
#     counter = start
#     while True:
#         yield counter
#         counter += step
# # Выводим с помощью функции next 10 элементов из бесконечно генерируемой последовательности начиная с 5 с шагом 4
# my_gen_func = count(5, 4)
# for i in range(10):
#     print(next(my_gen_func))


# # Создать генератор цикла, то есть в функцию на входе будет передаваться массив, например, [1, 2, 3], генератор будет
# # вечно работать возвращая 1 2 3 1 2 3… и так далее.
# def repeat_list(list_):
#    list_values = list_.copy()
#    while True:
#        value = list_values.pop(0)
#        list_values.append(value)
#        yield value
#
# for i in repeat_list([1, 2, 3]):
#    print(i)

# Итераторы
# для примера возьмём строку
# str_ = "my tst"
# str_iter = iter(str_)
#
# print(type(str_))  # строка
# print(type(str_iter))  # итератор строки
# # Получим первый элемент строки
# print(next(str_iter))  # m
#
# # Получим ещё несколько элементов последовательности
# print(next(str_iter))  # y
# print(next(str_iter))  #
# print(next(str_iter))  # t
# print(next(str_iter))  # s
# print(next(str_iter))  # t
# # Проверить, что будет происходить после окончания последовательности
# print(next(str_iter))


