sec_in = int(input("Введите количество секунд: "))
sec_out = sec_in % 60
min_in = sec_in // 60
min_out = min_in % 60
hour = min_in // 60
print(f"{hour}:{min_out}:{sec_out}")