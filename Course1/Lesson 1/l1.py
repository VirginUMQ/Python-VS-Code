print(2, 3, 4, "dsr")

n = 5
s = "saf"
f = 'fas'
print(n, f, s)

# type - показывает тип данных переменной

ty = 1
pe = "s"
print(type(ty), type(pe))

print(f"{n} - {s} - {f} - {ty} - {pe}") # print(f"текст {переменная} текст {переменная}")
# ИЛИ
print("{} - {}" .format(ty, pe))

# ВВОД ДАННЫХ input()

print("Как тебя зовут?")
name = input()
print("Привет,", name)
# ИЛИ
name2 = input("Дай мне имя: ")
print("Я -", name2)

r = range(0, 10, 2) # числа от 0 до 9 с шагом через 2
for i in r:
    print(i)



