import json

result = []
with open("json_task.json", "w", encoding="utf-8") as target:
    with open("text_7.txt", "r", encoding="utf-8") as my_file:
        profit = {}
        for line in my_file:
            profit[line.split()[0]] = int(line.split()[2]) - int(line.split()[3])
        avg_profit = sum([int(i) for i in profit.values() if int(i) > 0]) / len(
            [int(i) for i in profit.values() if int(i) > 0])
        result.append(profit)
        result.append({avg_profit: round(avg_profit)})
    json.dump(result, target)
