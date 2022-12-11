'''
1) Создайте интерактивный калькулятор.
Пользовательский ввод представляет собой формулу, состоящую из числа, оператора (+,-,*,/,**) и другого
числа, разделенных пробелом (например, 1 + 1). Проверьте input по следующим правилам:
1. Если входные данные не состоят из 3 действительных элементов, вызовите InputFormulaError, которая
является пользовательским исключением.
2. Если первый и третий элемент не являются действительными числами — выводится ошибка InputNumberError

3. Если второй элемент не соответствует поддерживаемым операторам — выводится ошибка InputOperatorError
Если ввод верен, выполните вычисление и выведите результат (в случае возникновения ошибки при 
вычислении — также выводим ее). Затем пользователю предлагается ввести новый ввод и так далее,
пока пользователь не введет quit.

Взаимодействие может выглядеть так:
>>> 1 + 1
2.0
>>> 3,2 - 1,5
1.70
>>> quit'''

# class InputNumberError(Exception):
#     pass
# class InputOperatorError(Exception):
#     pass
# class InputFormulaError(Exception):
#     pass

# print('Use quit for exit')
# while True:
#     a = input('Choice operator (+,-,*,/,**):').lower()
#     if a == 'quit':
#         break
#     if a in ('+', '-', '*', '/', '**'):
#         number1 = float(input('Number 1: '))
#         number2 = float(input('Number 2: '))
#         if number1 and number2 is not float:
#             raise InputNumberError
#         if a == '+':
#             print(number1 + number2)
#         elif a == '-':
#             print(number1 - number2)
#         elif a == '*':
#             print(number1 * number2)
#         elif a == '/':
#             try:
#                 number2 != 0
#                 print(number1 / number2)
#             except ZeroDivisionError:
#                 print('ZeroDivisionError')
#         elif a == '**':
#             print(number1 ** number2)
#     else:
#         print('InputOperatorError')


class InputNumberError(Exception):
    pass

class InputOperatorError(Exception):
    pass

class InputFormulaError(Exception):
    pass

operations={
        "+": lambda x,y: x + y,
        "-": lambda x,y: x - y,
        '*': lambda x,y: x * y,
        '/': lambda x,y: x / y,
        '**': lambda x,y: x**y 
        }


while True:
    s = input('Choice operator (+,-,*,/,**). Example"1 + 1":').lower()
    if s == 'quit':
        break
    a = s.split()
    if len(a) > 3:
        raise InputFormulaError
    print(a)
    try:
        len(a) > 3
        operation = operations[a[1]]
        number1 = float(a[0])
        number2 = float(a[2])
        print('{0:.2f}'.format(operation(number1, number2)))
    except KeyError:
        raise InputOperatorError
    except ValueError:
        raise InputNumberError

