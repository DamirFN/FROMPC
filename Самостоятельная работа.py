#Записать условие, которое является истинным, когда только одно из чисел А, В и С меньше 45. Иногда проще записать все
#условия и не пытаться упростить их.
A, B, C = int(input()), int(input()), int(input())
if (A < 45) and ((B >= 45) and ( C >= 45)):    #(A < 45) and ((B >= 45) and ( C >= 45)) or\
    print(True)
elif (B < 45) and ((B >= 45) and (C >= 45)):    #(B < 45) and ((B >= 45) and (C >= 45)) or\
    print(True)
elif (C < 45) and ((A >= 45) and (B >= 45)):    #(C < 45) and ((A >= 45) and (B >= 45)) or\
    print(True)
else:
    print(False)

#Записать логические выражения, которые определяют, что число А не принадлежит интервалу от -10 до -1 или интервалу
# от 2 до 15.
A = int(input())
if -10 <= A <= -1 or 2 <= A <=15:
    print('prenadlegit')
else:
    print('ne_prenadlegit')

#Дано двузначное число. Определить: входит ли в него цифра 5. Попробуйте решить её с использованием целочисленного
# деления и деления с остатком.
s = int(input())
a = s % 10
b = s // 10
if b == 5:
    print('Есть')
elif a == 5:
    print('Есть')
else:
    print('Нет')

#Проверить, все ли элементы в списке являются уникальными.
a = input('введите символы')
b = list(a)
print(b)
b = set(b)
print(b)
print(len(b))
print(len(set(b)))
if len(b) == len(set(b)):
    print("уникальный")
else:
    print('не уникальный')

#Дано натуральное восьмизначное число. Выясните, является ли оно палиндромом (читается одинаково слева направо и
# справа налево).
a = input('введите символы')
a = list(a)
b = a[::-1]
if a == b:
    print('палиндромом')
else:
    print('нет')

num = 12345678
if str(num) == str(num)[::-1]:
    print('палиндромом')
else:
    print('нет')