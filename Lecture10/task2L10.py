'''
Создать 2 класса Truck и Sedan, которые являются наследниками Auto.
Класс Truck имеет дополнительный обязательный атрибут max_load.
Переопределить метод drive, который перед появление сообщения «Car <brand> <mark> drives»
выводит сообщение «Attention!». 
Реализовать дополнительный метод load.
При его вызове происходит пауза в 1 секунду (используя модуль time), затем выводится сообщение «load»,
а затем снова происходит пауза в 1 секунду. 
Класс Sedan имеет дополнительный метод обязательный
атрибут max_speed и при вызове метода drive, после появления сообщения «Car <brand> <mark> drives»,
выводит сообщение «max speed of sedan <brand> <mark> is <max_speed>».
Инициализировать по 2 отдельных объекта этих классов, проверить работы их методов и атрибутов 
(вызвать методы, атрибуты вывести в печать)
'''

import time


class Auto:

    color = 'Green'
    weight = '1500 kg'

    def __init__(self,brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    def drive(self):
        print(f'Car {self.brand} {self.mark} drives')

    def stop(self):
        print(f'Car {self.brand} {self.mark} stop')

    def use(self):
        self.age += 1
        print(self.age)


class Truck(Auto):

    def __init__(self, brand, age, mark,max_load):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def drive(self):
        print('Attention')
        print(f'Car {self.brand} {self.mark} drives')

    def load(self):
        time.sleep(1)
        print('Load')
        time.sleep(1)



class Sedan(Auto):
    
    def __init__(self, brand, age, mark, max_speed):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def drive(self):
        print(f'Car {self.brand} {self.mark} drives')
        print(f'Max speed of sedan {self.brand} {self.mark} is {self.max_speed} km\h')



# car = Auto('Volvo',2003,'XC90')
# car.drive()
# car.stop()
# car.use()

t = Truck('Volvo', 2010, 'FH','12500')
s = Sedan('Volvo', 2002, 'S60', '200')
t.drive()
t.load()
s.drive()
s.use()
s.stop()

print(s.max_speed)
print(t.max_load)