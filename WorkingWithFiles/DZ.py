from csv import DictReader

with open("f_1.txt", 'w', encoding= 'utf-8') as f1:
    f1.write('F1\n===========\n----------\n********\n&&&&&&&&\n##########')

with open("f_2.txt", 'w', encoding= 'utf-8') as f2:
    f2.write('F2\n')

print('Созданы два файла')

def rFile(name):
    with open(name, 'r', encoding= 'utf-8') as fr:
        
        r = DictReader(fr)
        return list(r)

print('\nФайл 1:\n', rFile('f_1.txt'), "\n")
print('\nФайл 2:\n', rFile('f_2.txt'), "\n")

com = int(input('Выберите строку, которую нужно скопировать из первого файла и вставить во второй (1-5): '))
while True:
    if com >= 1 and com <= 5:
        break
    com = int(input('Введи от 1 до 5: '))


copy = open('f_1.txt', 'r', encoding= 'utf-8')
for i in range(0, com):
    copy.readline()
with open("f_2.txt", 'a', encoding= 'utf-8') as f2:
    
    f2.writelines(copy.readline())
copy.close()

print('\nФайл 2:\n', rFile('f_2.txt'), "\n")
