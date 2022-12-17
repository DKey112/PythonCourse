'''
Создайте генераторную функцию которая в качестве аргумента принимать путь к файлу «unsorted_names.txt» и 
букву английского алфавита,открывает файл по данному пути и генерирует последовательность из
имен начинающихся на указанную букву
'''



def names_gen(path, later):
    with open (path, 'r') as file:
        for i in file:
            if i.startswith (later):
                yield i


name = names_gen('D:\\PythonCourse\\PythonCourse\\Lecture13\\unsorted_names.txt', 'A')
next(name)
for i in name:
    print(i)