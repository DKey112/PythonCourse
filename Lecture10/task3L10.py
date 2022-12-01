'''
Реализуйте класс Counter, который дополнительно принимает начальное значение и конечное значение счетчика.
Если начальное значение не указано, счетчик должен начинаться с 0.
Если стоп-значение не указано, оно должно считаться вверх бесконечно.
Если счетчик достигает стоп-значения, выведите «Maximal value is reached».
Реализовать методы: "increment" (увеличивает счетчик на 1) и "get" (выводит информацию о значении счетчика)
Пример:
c = Counter(start=42)
c.increment()
c.get()
43
'''

class Counter:
    
    def __init__(self, start =0, stop = -1):
        self.start = start
        self.stop = stop
        # self.start += 1

    def increment(self):
        # self.start += 1
        if self.start == self.stop:
            return print('Maximal value is reached')
        else:
            self.start += 1
        


    def get(self):
        return self.start




c = Counter(start=42)
c.increment()
c.get()

c = Counter()
c.increment()
c.get()

c.increment()
c.get()


c = Counter(start=42, stop=43)
c.increment()
c.get()

c.increment()

c.get()

