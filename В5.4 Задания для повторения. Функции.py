# Решение уровнения с одним неизвестным
# def linear_solve(a, b):
#     if a:
#         return b / a
#     elif not a and not b: # снова используем числа в логических выражениях
#         return "Бесконечное количество корней"
#     else:
#         return "Нет корней"
# print(linear_solve(0, 1))

# Решение квадратного уровнения
# a*x**2 + b*x + c = 0 - общий вид уравнения
# D = b**2 - 4*a*c - дискриминант
# Если D<0, то уравнение не имеет вещественных корней
# Если D=0, то уравнение имеет один корень - x = -b/(2*a)
# Если D>0, то уравнение имеет два корня
# x1 = (-b - D**0.5)/(2*a)
# x2 = (-b + D**0.5)/(2*a)
#
# P.S. D**0.5 - равносильно извлечению квадратного корня

# def disc(a, b, c):
#     D = pow(b, 2) - 4 * a * c
#     x1 = (-b - D**0.5)/(2*a)
#     x2 = (-b + D**0.5) / (2 * a)
#     x = -b / (2 * a)
#     if D < 0:
#         print('Уравнение не имеет вещественных корней')
#     elif D == 0:
#         print('Уравнение имеет один корень', round(x, 2))
#     elif D > 0:
#         print('Уравнение имеет два кореня', round(x1, 2), round(x2, 2))
#     return D
#
# disc(2, 7, 0)

# def quadratic_solve(a, b, c):
#     if D(a, b, c) < 0:
#         return "Нет вещественных корней"
#     elif D(a, b, c) == 0:
#         return -b / (2 * a)
#     else:
#         return (-b - D(a,b,c) ** 0.5) / (2 * a), (-b + D(a, b, c) ** 0.5) / (2 * a)

# Итерация объекта
# iter_obj = iter("Hello!")
#
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

# Декоратор
# Авторизация пользователя
yesno = input("""Введите Y, если хотите авторизоваться, или N,
             если хотите продолжить работу как анонимный пользователь: """)

auth = yesno == "Y"
def is_auth(func):
    def wrapper():
        if auth:
            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь не авторизован. Функция выполнена не будет")
    return wrapper
@is_auth
def from_db():
    print("some data from database")
from_db()
@is_auth
def change_profile():
    print("Profile has been changed")
change_profile()

# USERS = ['admin', 'guest', 'director', 'root', 'superstar']
#
# yesno = input("""Введите Y, если хотите авторизоваться, или N,
#              если хотите продолжить работу как анонимный пользователь: """)
#
# auth = yesno == "Y"
# def is_auth(func):
#     def wrapper():
#         if auth:
#             print("Пользователь авторизован")
#             func()
#         else:
#             print("Пользователь не авторизован. Функция выполнена не будет")
#     return wrapper
# if auth:
#     username = input("Введите ваш username:")
#     def has_access(func):
#         def wrapper():
#
#             if username == USERS:
#                 print('Вход разрешен')
#                 func()
#             else:
#                 print("Доступ пользователю", username, "запрещён")
#
#         return wrapper
#
# @is_auth
# @has_access
# def from_db():
#     print("some data from database")
#
# from_db()
