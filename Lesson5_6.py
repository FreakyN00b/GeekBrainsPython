item = {}
with open("text_6.txt", "r", encoding="utf-8") as my_file:
    for i in my_file:
        total_time = []
        all_subj = ([el for el in i.split(" ")])
        for el in all_subj:
            total_time.append("".join(i for i in list(el) if i.isdigit()))
        item[i.split(":")[0]] = sum([int(i) for i in total_time if i.isdigit()])

print(item)