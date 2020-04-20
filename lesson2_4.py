my_str = input("Введите несколько слов, разделенных пробелами- ").split()
str_num = 1
for i in my_str:
    if int(len(i)) <= 0:
        print(f"{str_num}) {i}")
        str_num += 1
    else:
        print(f"{str_num}) {i[0:9]}")
        str_num += 1