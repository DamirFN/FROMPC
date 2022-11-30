#Так выглядит тело функции
# def name_func():    #der - объявлениие функции, name_func() - название функции
#     # начало тела функции
#     ...
#     # конец тела функции
#
# #Напишите функцию print_2_add_2, которая будет складывать 2 и 2 и печатать этот результат.
# def print_2_add_2():
#     sum_ = 2 + 2
#     print(sum_)
#
#
# print_2_add_2()

# def Begrusung():
#     str_ = 'Hello World'
#     print(str_)
# Begrusung()
#
# oder
# def Begrusung():
#     print('Hello World')
# Begrusung()

# объявили функцию для подсчёта количества символов в неком абстрактном тексте
# def char_frequency(text):
#    text = text.lower()
#    text = text.replace(" ", "")
#    text = text.replace("\n", "")
#
#    count = {}  # для подсчёта символов и их количества
#    for char in text:
#        if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#            count[char] += 1
#        else:
#            count[char] = 1
#
#    for char, cnt in count.items():
#        print(f"Символ {char} встречается {cnt} раз")

#Функция возведение любой переменной в любую степень, но по умолчанию во 2
# def pow_funk(base, n=2):    #argumente base und n=2(Default, Standartgrat)
#     print(base**n)
# pow_funk(3, 10)

#Prüfung: ob die Zahl n ein Teiler der Zahl a ist und zeigt die entsprechende(соответственное) Meldung auf dem
# Bildschirm an, ob die Zahl ein Teiler(делителем) ist oder nicht.
# def teil_von_zahl(zahl_a, teil_n):
#     if zahl_a % teil_n == 0:
#         print(f'Ja, genau!, {teil_n} ist Teil für {zahl_a}')
#     else:
#         print('Probiren Sie andere Teil!')
# zahl_a = int(input('nehmen sie eine Zahl'))
# teil_n = int(input('die Teil für Ihre Zahl')
# teil_von_zahl(zahl_a, teil_n)

#Schreiben Sie eine Funktion, die eine "umgekehrte Leiter" wie folgt druckt:
# def umgekehrte_leiter(Anzahl_der_Schritte):
#     print(f'Höhe und langvon umgekehrte Leiter {Anzahl_der_Schritte} auf {Anzahl_der_Schritte}')
#     for Anzahl_der_Schritte in range(Anzahl_der_Schritte, 0, -1):
#         print('*' * Anzahl_der_Schritte)
#
# Anzahl_der_Schritte = int(input('Anzahl_der_Schritte'))
# umgekehrte_leiter(Anzahl_der_Schritte)

#Schreiben Sie eine Funktion, die die Anzahl der Teiler von a zurückgibt.
# def Zahl_der_Teil_von_Zahl_a(a):
#     count = 0
#     for Zahlen_teil in range(1, a+1):
#         if a % Zahlen_teil == 0:
#             count += 1
#     return count
# #
# c = Zahl_der_Teil_von_Zahl_a(5)
# print(c)

# # Проверяем текст на полиндромность(зеркальность)
# def heck_palindrome(text):
#     text = text.replace(' ', '')
#     text = text.lower()
#     text = text.replace('\n', '')
#     if text == text[::-1]:
#         # print(f'Текст {text} является палиндромом')
#         return True     #возвращаем ответ True при верном условии
#     else:
#         return False    #возвращаем ответ False при не оправдавшемся условии
#
# c = heck_palindrome('vepd')     #Заносим наш возвращенный ответ в переменную c
# print(c)    #печатаем возвращенный ответ
# b = heck_palindrome('Кит на море не романтик')
# print(b)








