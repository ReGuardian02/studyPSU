import cmath
import math
import random


class Calculator:
    def __init__(self):
        pass

    def plus(self):
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
        return a + b

    def minus(self):
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
        return a - b

    def multiply(self):
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
        return a * b

    def divide(self):
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
        return a / b

    def exp(self):
        a = float(input('Введите число: '))
        b = float(input('Введите степень числа: '))
        return a ** b

    def rand(self):
        return random.randint(0, 1000)

    def factorial(self):
        a = int(input('Введите число: '))
        return math.factorial(a)

    def arccos(self):
        a = float(input('Введите число: '))
        return cmath.acos(a)

    def main(self):
        proc = str(input('Введите один из знаков опрации: [+, -, *, /, x^n, random, !, acos] '))
        if proc == '+':
            answ = calc.plus()
            print(answ)
        elif proc == '-':
            answ = calc.minus()
            print(answ)
        elif proc == '*':
            answ = calc.multiply()
            print(answ)
        elif proc == '/':
            answ = calc.divide()
            print(answ)
        elif proc == 'x^n':
            answ = calc.exp()
            print(answ)
        elif proc == 'random':
            answ = calc.rand()
            print(answ)
        elif proc == '!':
            answ = calc.factorial()
            print(answ)
        elif proc == 'acos':
            answ = calc.arccos()
            print(answ)


calc = Calculator()
calc.main()