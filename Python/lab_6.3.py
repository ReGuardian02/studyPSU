import cmath
import random

proc = input('Введите один из знаков опрации: [+, -, *, /, x^n, random, !, acos] ')

def plus():
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    return a + b

def minus():
    a = float(input('Введите первое число'))
    b = float(input('Введите второе число'))
    return a - b

def multiply():
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    return a * b

def divide():
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    return a / b

def exp():
    a = float(input('Введите число: '))
    b = float(input('Введите степень числа: '))
    return a ** b

def rand():
    return random.randint(0, 1000)

def factorial():
    a = int(input('Введите число: '))
    return cmath.factorial(a)

def arccos():
    a = float(input('Введите число: '))
    return cmath.acos(a)

if proc == '+':
    answ = plus()
    print(answ)
elif proc == '-':
    answ = minus()
    print(answ)
elif proc == '*':
    answ = multiply()
    print(answ)
elif proc == '/':
    answ = divide()
    print(answ)
elif proc == 'x^n':
    answ = exp()
    print(answ)
elif proc == 'random':
    answ = rand()
    print(answ)
elif proc == '!':
    answ = factorial()
    print(answ)
elif proc == 'acos':
    answ = arccos()
    print(answ)