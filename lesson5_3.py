with open("text_3.txt", "r", encoding="utf-8") as text:
    not_enough = []
    salary = []
    line = text.read().split("\n")
    for i in line:
        i = i.split()
        if float(i[1]) < 20000:
            not_enough.append(i[0])
        salary.append(i[1])
    average = sum(map(float, salary)) / len(salary)
print(f"Оклад меньше 20000р: {not_enough}\nСредняя зарплата: {average}")
