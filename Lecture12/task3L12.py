'''
Создайте класс, который имеет атрибут queue (допускается использование списка) который имеет метод add позволяющий добавлять
в queue следующие объекты — целые числа, числа с плавающей запятой, строки. При этом в момент добавления происходит валидация 
элементов по следующим правилам:
1. Целые числа — должны делится на 8, состоять из не более чем 4 символов
2. Числа с запятой — не более 3 символов после запятой
3. Строки — длина не более 4 символов без дублирования символов
В результате работы метода add элементы прошедшие валидацию добавляются в queuе, элементы не прошедшие валидацию  выводятся пользователю с сообщением о причине недобавления, например 
q=Queue()
q.add(1, 16, 280, 80000, 2.51, 1.875, text, data, world)
InvalidIntDivision → 1 # не делится на 8
InvalidIntNumberCount → 80000 # больше 4 символов
InvalidFloat → 1.875 # больше 2 символов после запятой
InvalidTextLength → world # больше 4 символов
DuplicatesInText → data # повторяющиеся символы
q.queue
# [16,280,text]
!!! название ошибок можно выбрать самостоятельно !!!
'''


class InvalidIntDivision(Exception):
    ...


class InvalidIntNumberCount(Exception):
    ...


class InvalidFloatNumber(Exception):
    ...


class InvalidTextLength(Exception):
    ...
class DuplicatesInText(Exception):
    ...

class Queue:
    def __init__(self):
        self.queue = []


    def add(self,*args):
        try:
            for i in args:
                if isinstance(i, int):
                    if i % 8 == 0: # Проверка деление числа на 8
                        if len(str(i)) <= 4:   # Проверка на длину вводимого числа 
                            self.queue.append(i) 
                        else:
                            raise InvalidIntNumberCount  
                    else:
                        raise InvalidIntDivision
                elif isinstance(i, float):  
                    s = str(i)  
                    index = s.find(".")  
                    s = s[index + 1:]  
                    if len(s) <= 3:  
                        self.queue.append(i)
                    else:  
                        raise InvalidFloatNumber
                elif type(i) == str:
                    s = ''
                    for c in i:
                        if c not in s:
                            s += c
                        if len(s) < 2:
                            self.queue.append(i)
                        else: 
                            raise DuplicatesInText
                        if len(i) <= 4: 
                            self.queue.append(i)  
                        else:
                            raise InvalidTextLength  
        except InvalidIntDivision:
            print(f'{i} -> Не делится на 8')
        except InvalidIntNumberCount:
            print(f'{i} ->-> Больше 4 символов')
        except InvalidFloatNumber:
            print(f'{i} -> Больше 3 символов после запятой')
        except InvalidTextLength:
            print(f'{i} -> Больше 4 символов')
        except DuplicatesInText:
            print(f'{i} -> Дублирование символа')

q = Queue()
q.add(16, 280, 1.82, "wordd", 1.8345, "text", 80000)
print(q.queue)