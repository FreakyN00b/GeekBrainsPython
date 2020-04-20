number = int(input("Введите целое положительное число: "))
check = number % 10
new_number = number // 10
num_max = number % 10
while number > 0:
    if number % 10 > num_max:
        num_max = number % 10
    number = number // 10
print(f"Самая большая цифра в числе: {num_max}")