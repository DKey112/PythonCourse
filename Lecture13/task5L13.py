'''
Реализуйте генератор, который будет бесконечно генерировать числа Фибоначчи (https://en.wikipedia.org/wiki/Fibonacci_number).
Пример:
>>> gen = endless_fib_generator()
>>> while True:
	print(next(gen))
>>> 1 1 2 3 5 8 13 ...
'''

def endless_fib_generator():
    fb1 = int(input('Enter number 1: '))
    fb2 = int(input('Enter number 2: '))

    while True:
        yield fb1
        fb1, fb2 = fb2, fb1 + fb2


gen = endless_fib_generator()
while True:
	print(next(gen))