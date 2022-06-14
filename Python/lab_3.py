import math
import random

oper = input('Введите один из знаков опрации: [+, -, *, /, x^n, random, !, acos] ')

if oper == '+':
    print('Введите первое число ')
    a = int(input())
    print('Введите второе число ')
    b = int(input())
    с = a+b
    print('Ответ: ',с)
elif oper == '-':
    print('Введите первое число ')
    a = int(input())
    print('Введите второе число ')
    b = int(input())
    с = a-b
    print('Ответ: ',с)
elif oper == '*':
    print('Введите первое число ')
    a = int(input())
    print('Введите второе число ')
    b = int(input())
    с = a * b
    print('Ответ: ',с)
elif oper == '/':
    print('Введите первое число ')
    a = float(input())
    print('Введите второе число ')
    b = float(input())
    с = a/b
    print('Ответ: ',с)
elif oper == 'x^n':
    print('Введите число ')
    a = int(input())
    print('Введите степень числа ')
    b = int(input())
    с = a ** b
    print('Ответ: ',с)
elif oper == 'random':
   print(random.randint(0,1000))
elif oper == '!':
    print('Введите число ')
    a = int(input())
    с = math.factorial(a)
    print('Ответ: ', с)
elif oper == 'acos':
    print('Введите число ')
    a = float(input())
    с = math.acos(a)
    print('Ответ: ', с)