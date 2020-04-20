all_months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
value = int(input("Введите порядковый номер месяца: "))
if all_months.index(value) == -1 or all_months.index(value) == 1 or all_months.index(value) == 2:
    print("It is a frosty winter now!")
elif all_months.index(value) == 3 or all_months.index(value) == 4 or all_months.index(value) == 5:
    print("It is spring!")
elif all_months.index(value) == 6 or all_months.index(value) ==7 or all_months.index(value) == 8:
    print("It is summertime...")
elif all_months.index(value) == 9 or all_months.index(value) == 10 or all_months.index(value) == 11:
    print("It is fall")
#
#
#
all_months = {12: "winter", 1: "winter", 2: "winter",
              3: "spring", 4: "spring", 5: "spring",
              6: "summer", 7: "summer", 8: "summer",
              9: "fall", 10: "fall", 11: "fall"}
value = int(input("Введите порядковый номер месяца: "))
print(all_months.get(value))