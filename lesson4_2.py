my_list = [45, 40, 7, 6, 4, 7, 20, 1, 3, 5, 99]
new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {new_list}')