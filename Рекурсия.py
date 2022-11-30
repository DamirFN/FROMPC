# С помощью рекурсивной функции найдите сумму чисел от 1 до n.
def rec_sum(n):
    if n == 1:
        return 1
    return n * rec_sum(n-1)
p = rec_sum(3)
print(p)

#С помощью рекурсивной функции разверните строку.
def reverse_str(string):
   if len(string) == 0:
       return ''
   else:
       return string[-1] + reverse_str(string[:-1])

c = reverse_str('test')
print(c)# tset

# Дано натуральное число N. Вычислите сумму его цифр.
def sum_digit(n):
   if n < 10:
       return n
   else:
       return n % 10 + sum_digit(n // 10)

r = sum_digit(9)
print(r)

v = 155
y = 15
u = v % 10 + v // 10 + 15//10
print(u)