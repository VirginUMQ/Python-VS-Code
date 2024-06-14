from csv import DictReader, DictWriter
from os.path import exists


def get_info():
    first_name = "Иван"
    second_name = "Иванов"
    phone = "89999999999"
    return [first_name, second_name, phone]



def create_file(f_name):
    with open(f_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone'])
        f_w.writeheader()



def write_file(f_name):
    user_data = get_info()
    res = read_file(f_name)
    new_obj = {'first_name': user_data[0], 'second_name': user_data[1], 'phone': user_data[2]}
    res.append(new_obj)



    with open(f_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone'])
        f_w.writeheader()
        f_w.writerows(res)



def read_file(f_name):
    with open(f_name, encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r) 



f_name = 'phone.csv'



def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(f_name):
                create_file(f_name)
            write_file(f_name)
        elif command == 'r':
            if not exists(f_name):
                print("Сначала создайте файл")
                continue
            print(*read_file(f_name))



main()