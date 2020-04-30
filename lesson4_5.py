from functools import reduce


def my_func(num_1, num_2):
    return num_1 * num_2

my_list = [i for i in range(100, 1001, 2)]
print(f"List of all numbers: {my_list}\nResult of multiplication: {reduce(my_func, my_list)}")