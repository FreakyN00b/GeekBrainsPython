goods = []
str_num = 0
while input("Вы хотите добавить новый товар? (да\нет)") == "да":
    while input("Вы хотите ввести характеристики товара? (да\нет)") == "да":
        str_num += 1
        specifications = {}
        name_val = input("Укажите название товара: ")
        name_key = "Название"
        price_val = input("Укажите стоимость товара: ")
        price_key = "Цена"
        count_val = input("Укажите количество товара: ")
        count_key = "Количество"
        features_val = input("Укажите единицу измерения: ")
        features_key = "Единица измерения"
        specifications = {name_key: name_val, price_key: price_val, count_key: count_val, features_key: features_val}
        goods.append(tuple([str_num, specifications]))
for i in goods:
    print(i)
if input("Желаете ли вывести аналитику по всем товарам? (да\нет)") == "да":
    analitics = {}
    for i in goods:
        for dict_key, dict_val in i[1].items():
            if dict_key in analitics:
                analitics[dict_key].append(dict_val)
            else:
                analitics[dict_key] = [dict_val]
print(analitics)
