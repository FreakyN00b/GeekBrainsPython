from random import randint

total = 0
with open("task_5.txt", "w") as my_file:
    for i in range(100):
        num = randint(1, 100)
        total += num
        my_file.writelines(str(num) + "\n")
print(total)
