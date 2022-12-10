'''
Реализуйте класс итератора EvenRange, который принимает начало и конец интервала в качестве аргументов инициализации 
и выдает только четные числа во время итерации.
Если пользователь попытается выполнить итерацию после того, как он выдал все возможные числа следует вывести «Out of number!».
_Пpимeчaниe: вообще не используйте функцию range()_
Пример:
>>> er1 = EvenRange(7,11)
next(er1)
>>> 8
next(er1)
>>> 10
next(er1)
>>> "Out of numbers!"
next(er1)
>>> "Out of numbers!"
>>> er2 = EvenRange(3, 14)
>>> for number in er2:
    print(number)
>>> 4 6 8 10 12 "Out of numbers!"
'''

class EvenRange:

    
    def __init__(self, start, end):
        self.start = start if not start % 2 else start + 1
        self.end = end


    def __iter__(self) :
        return self



    def __next__(self):
        result=self.start
        if result < self.end:
            self.start += 2
            print(result)
            return result
        else:
            print('Out of numbers')
            raise StopIteration


# er1 = EvenRange(7,11)
# next(er1)
# next(er1)
# next(er1)
# next(er1)

er2 = EvenRange(3, 14)
for number in er2:
    print(number)