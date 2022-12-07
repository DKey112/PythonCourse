'''
Реализуйте класс DataObject который имеет обязательный атрибут data (произвольного типа данных)
Реализуйте класс очередь (Deque) с атрибутом класса deque в котором будут хранится элементы 
добавляемые в очередь,Класс Deque имеет методы 
- append_left для добавления элемента в начало очереди deque
- append_right для добавления элемента в конец очереди deque
(в данных методах необходимо реализовать возможность добавления в очередь только экземпляров класса
DataObject (и его дочерних), а также проверку длины очереди — одновременно там может находится не 
более 5 элементов — в случае добавления 6 элемента добавление не производится и пользователю 
выдается сообщение о переполнении очереди). 
- pop_left — удаляет из очереди первый элемент слева и возвращает его
- pop_right - удаляет из очереди первый элемент справа и возвращает его
При реализации методов класса Deque воспользуйтесь методами класса (classmethod)
'''
from typing import Any
from dataclasses import dataclass

@dataclass
class DataObject:
    data : Any


some_data1 = DataObject(10)
some_data2 = DataObject(15)
some_data3 = DataObject(20)


class Deque:

    # def __init__(self):
    #     self.lst = []
    lst=[]
    
    @classmethod
    def append_left(cls,some_cls):
        if isinstance(some_cls, DataObject):
            if len(cls.lst) < 5:
                cls.lst.insert(0,some_cls.data)
                # print(cls.lst)
                return cls.lst
            else:
                print(f'Очередь переполнена, удалите 1 элемент: {cls.lst}')


        
    @classmethod
    def append_right(cls,some_cls):
        if isinstance(some_cls, DataObject):
            if len(cls.lst) < 5:
                    cls.lst.append(some_cls.data)
                    # print(cls.lst)
                    return cls.lst
            else:
                print(f'Очередь переполнена, удалите 1 элемент: {cls.lst}')

    @classmethod
    def pop_left(cls):
        del cls.lst[0]
        return cls.lst

    @classmethod
    def pop_right(cls):
        del cls.lst[-1]
        return cls.lst

print(Deque.append_left(some_data1))
print(Deque.append_left(some_data2))
print(Deque.append_left(some_data3))
print(Deque.append_left(some_data3))
print(Deque.append_left(some_data2))
print(Deque.append_left(some_data1))

# print(Deque.append_right(some_data1))
# print(Deque.append_right(some_data2))
# print(Deque.append_right(some_data3))
# print(Deque.append_right(some_data3))
# print(Deque.append_right(some_data2))


print(Deque.pop_right())
print(Deque.pop_left())
print(Deque.pop_right())