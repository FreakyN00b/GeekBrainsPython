ru_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_line = []
with open("text_4.txt", "r") as my_file:
    line = my_file.read().split("\n")
    for i in line:
        i = i.split(" - ")
        new_line.append(ru_dict[i[0]] + " " + i[1] + "\n")

with open("text_4_4.txt", "w") as new_file:
    new_file.writelines(new_line)