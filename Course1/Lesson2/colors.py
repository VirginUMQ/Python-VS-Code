# МНОЖЕСТВА

c = set() # создать пустое множество
print(c)

c = {"red", "black", "white"} # создать множество

print(c)
c.add("yellow")
print(c)
c.remove("red")  # удалить "red" , но если его не было раньше, то будет ошибка
print(c)
c.discard("red") # удалить "red" , но если его не было, то пропустит строку кода
print(c)
c.clear() # удалить все элементы
print(c)

b = frozenset(c) # создать замороженное множество, которое нельзя изменять
print(b)
