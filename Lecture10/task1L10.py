'''
1. Создать родительский класс Auto, у которого есть атрибуты: brand, age, color, mark и weight.
В классе должны быть реализованы следующие методы — drive, use и stop. 
Методы drive и stop выводят сообщение «Car <brand> <mark> drives / stops».
Метод use увеличивает атрибут age на 1 год.
Атрибуты brand, age и mark необходимо инициализировать при объявлении объекта
'''

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
        print(f'Car{self.brand} {self.mark} stop')

    def use(self):
        self.age += 1
        print(self.age)

car = Auto('Volvo',2003,'XC90')
car.drive()
car.stop()
car.use()
