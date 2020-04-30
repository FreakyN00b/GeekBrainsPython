from itertools import count

for el in count(int(input('Введите стартовое число  или введите q для завершения программы: '))):
    print(el, end="")
    exit = input()
    if exit == "q" or exit == "Q":
        break

from itertools import cycle

my_list = input("Введите элементы, разделяя их пробелом: ").split()
el = cycle(my_list)
exit = None

while exit != "q" or exit != "Q":
    print(next(el), end="")
    exit = input()
