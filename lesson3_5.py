def my_sum():
    sum_res = 0
    exit = False
    while exit == False:
        numbers = input("Введите число или нажмите Q для выхода: ").split()
        res = 0
        for i in range(len(numbers)):
            if numbers[i] == 'q' or numbers[i] == 'Q':
                exit = True
                break
            else:
                res = res + int(numbers[i])
        sum_res = sum_res + res
        print(f"Сумма чисел на текущий момент: {sum_res}")
    print(f"Итоговая сумма:  {sum_res}")


my_sum()
