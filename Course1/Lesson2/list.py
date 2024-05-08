#  СПИСКИ 
list_1 = [] # создать пустой список

list_2 = list() # создать пустой список
print(list_1, list_2)
list_3 = [3, 5, 6]
print(list_3)
print(*list_3) # убрать символы
list_3.append(9) # добавить значение в список
print(*list_3)


list_4 = []           # создать список от 0 до 4
print(list_4)
for i in range(5):    # создать список от 0 до 4
    list_4.append(i)  # создать список от 0 до 4
    print(list_4)

print(list_4.pop(), list_4)  # .pop() удалить последний элемент в списке

print(list_4.pop(0), list_4) # .pop(0) удалить 0 элемент в списке

print(list_4.insert(3, 4), list_4) # добавить элемент "4" на позицию индекса 3


# ЗАДАЧА СОСТАВИТЬ СПИСОК 1-100

list_5 = [i for i in range(1, 101)]
print(*list_5, "\n")

# ТОЛЬКО ЧЕТНЫЕ

list_6 = [i for i in range(1, 101) if i % 2 == 0]
print(*list_6, "\n")

# ПАРЫ ДЛЯ КАЖДОГО ЧИСЛА

list_7 = [(i, i) for i in range(1, 101) if i % 2 == 0]
print(*list_7)


