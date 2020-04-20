value = int(input("Введите натуральное число: "))
my_list = [9, 7, 5, 4, 2, ]
counter = my_list.count(value)
for el in my_list:
    if counter > 0:
        i = my_list.index(value)
        my_list.insert(i + counter, value)
        break
    else:
        if value > el:
            n = my_list.index(el)
            my_list.insert(n, value)
            break
        elif value < my_list[len(my_list)]:
            my_list.append(value)
print(my_list)
