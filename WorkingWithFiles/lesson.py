def delenie (delenie, a, b):
    return(delenie(a,b))

# def calk1 (a,b):
#     return a+b

calk1 = lambda a, b: a + b

a = calk1(2, 3)
b = calk1(a, a)

print("a =", a, "\nb =", b)

print("b / a =", delenie(lambda a,b: b/a,a,b))


# Выбрать четные числа в списке и составить список пар (число, квадрат)

# def chetList(num):
#     newnum = []
#     for i in num:
#         if i % 2 == 0:
#             newnum.append((i, i**2))
#     return newnum

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(chetList(num))

def select (f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)


# ================ MAP - функция переборки - (передаем функцию которую нужно выполнить, сам объект) 

li = [x for x in range(1, 10)]
print(li)

li = list(map(lambda x: x + 10, li))
print(li)



# list строк в list чисел

nums = "1 2 3 4 5 44 33 22 11"
print(nums)
# nums = nums.split()
# print(nums)

nums = list(map(int, nums.split()))
print(nums)



# =============================== FILTER - фильтрация - передаем функцию и объект
spisok = [14, 55, 34, 35, 6, 5]
print(spisok)
res5 = list(filter(lambda x: x % 10 == 5, spisok))
print(res5)



# ============================== ZIP - функция, которая из 3 списков делает кортеж 
rus = ['а', 'б', 'в']
n = [1, 2, 3]
eng = ['a', 'b', 'c']
RNE = list(zip(rus, n, eng))
print(RNE)



# ===================== ENUMERATE - принимает список и возвращает кортеж индекс+элемент 

enu = ["A", "B", "C"]
enu = list(enumerate(enu))
print(enu)



# ========================================== ФАЙЛЫ ==========================================
# РЕЖИМЫ РАБОТЫ С ФАЙЛАМИ:

# a - открытие для добавления данных
# позволяет дописывать в файл, если файл не существует, то сначала создаст и в него начнется запись

# r - открытие для чтения
# позволяет читать файл, если файл не существует то выдаст ошибку

# w - открытие для записи данных
# позволяет записывать данные и создавать файл, если его не существует 
# если файл существовал, то данные удалятся и будут записываться заново

# w+ - открыть файл для записи и читать из него
# если файл не существует то он будет создан

# r+ - позволяет читать файл и дописывать в него
# если файл не существует, то выдаст ошибку



colors = ['BLUE', 'RED', 'BLACK']
openFile = open('file.txt', 'a', encoding='utf-8') # переменная(oppenFile) = open(название, режим, необязательно(кодировка)) - открыть/создать файл
openFile.writelines(colors)
openFile.close()


with open('file2.txt', 'w') as openFile2:   # with open(название, режим) as Переменная
                                            # чтобы каждый раз не открывать, не закрывать
    openFile2.write('line 1\n')
    openFile2.write('line 2\n')


openFile3 = open('file.txt', 'r')
for line in openFile3:
    print(line)
openFile3.close()

openFile3 = open('file2.txt', 'r')
for line in openFile3:
    print(line)
openFile3.close()



#  ================================ МОДУЛЬ os ==========================================
# модуль нужно импортировать

import os
# базовые функции модуля:

# os.chdir('путь') - смена текущей директории ('C:Users:File')

road = os.getcwd() # - получить путь текужей директории
print("Директория находится по адресу:", road )



# os.path() # - вложенный модуль в модуль os:

# print(os.path.basename('C:\Users\Admin\Desktop\Python VS Code')) # - базовое имя пути 

# os.path.abspath(файл) - возвращает нормальзованный абсолютный путь
print("Нормальзованный абсолютный путь file.txt:", os.path.abspath('file.txt'))



# =============================== МОДУЛЬ SHUTIL ===================================
# сначала импорт
import shutil

# БАЗОВЫЕ ФУНКЦИИ:

# shutil.copyfile(src, dst) - копирует содержимое (но не метаданные) файла src в файл dst 

# shutil.copy(src, dst) - копирует содержимое файла src в файл или папку dst 

# shutil.rmtree(path) - удаляет текущую директорию и все поддиректории; path должен указывать
# на директорию, а не на символическую ссылку