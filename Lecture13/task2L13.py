'''
Реализуйте свой пользовательский класс итератора c именем MySquareIterator, 
который дает квадраты элементов коллекции, по которой он итерируется.
>>> lst = [1, 2, 3, 4, 5]
>>> itr = MySquareIterator(lst)
>>> for el in itr:
    print(el)
>>> 1 4 9 16 25

'''

class MySquareIterator:
    
    def __init__(self, obj):
        self.list = obj
        self.index = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            i = self.list[self.index]
        except IndexError:
            raise StopIteration
        else:
            self.index += 1
            return i**2

lst = [1, 2, 3, 4, 5]
itr = MySquareIterator(lst)

for i in itr:
    print(i, end=' ')