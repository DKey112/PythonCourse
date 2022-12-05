'''
Реализуйте класс который представляет собой универсальный интерфейс по представлению температуры 
в шкалах Цельсия/Кельвина/Фаренгейта и поддерживает конвертацию значений температуры между этими
шкалами (https://www.cuemath.com/temperature-conversion-formulas/)
'''



class Temp:
    
    def __init__(self) -> int:
        self.C = 0
        self.K = 273
        self.F = 32

    def Celsius(self, C) -> float:
        self.C = print(f'Celsius: {C}')
        self.K = print(f'Celsius to Kelvin: {C + self.K}')
        self.F = print(f'Celsius to Fahrenheit: {C * (9 / 5) + 32}')
    
    def Kelvin(self, K) -> float:
        self.K = print(f'Kelvin: {K}')
        self.C = print(f'Kelvin to Celsius: {K - 273}')
        self.F = print(f'Kelvin to Fahrenheit: {(K - 273) * (9 / 5) + 32}')

    
    def Fahrenheit(self, F) -> float:
        self.F = print(f'Fahrenheit: {F}')
        self.C = print(f'Fahrenheit to Celsius: {(F - 32) * (5 / 9)}')
        self.K = print(f'Fahrenheit to Kelvin: {F * (9 / 5) + 32}')


swap = Temp()
swap.Celsius(15)
swap.Kelvin(295)
swap.Fahrenheit(35)
