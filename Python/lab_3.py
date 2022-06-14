import cmath
import random

oper = input('Введите один из знаков опрации: [+, -, *, /, x^n, random, !, acos] ')

if oper == '+':
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    с = a+b
    print('Ответ: ',с)
elif oper == '-':
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    с = a-b
    print('Ответ: ',с)
elif oper == '*':
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    с = a * b
    print('Ответ: ',с)
elif oper == '/':
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    с = a/b
    print('Ответ: ',с)
elif oper == 'x^n':
    a = int(input('Введите число: '))
    b = int(input('Введите степень числа: '))
    с = a ** b
    print('Ответ: ',с)
elif oper == 'random':
   print(random.randint(0,1000))
elif oper == '!':
    a = int(input('Введите число: '))
    с = cmath.factorial(a)
    print('Ответ: ', с)
elif oper == 'acos':
    a = float(input('Введите число: '))
    с = cmath.acos(a)
    print('Ответ: ', с)