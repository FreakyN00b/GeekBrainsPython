from random import randint

my_list = [randint(0, 50) for i in range(15)]
unic_els = [el for el in my_list if my_list.count(el) < 2]
print(unic_els)