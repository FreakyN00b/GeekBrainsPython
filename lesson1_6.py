distanceFirstDay = int(input("Сколько километров пробежал спортсмен в первый день? "))
totalDistance = int(input("Сколько километров должен пробежать спортсмен? "))
day = 1
distancePerDay = distanceFirstDay + (distanceFirstDay / 100 * 10)
while distancePerDay <= totalDistance:
    print(f"{day}-й день: {distancePerDay:.2f} километров")
    day += 1
    distancePerDay = distancePerDay + (distancePerDay / 100 * 10)
    if distancePerDay > totalDistance:
        print(f"{day}-й день {distancePerDay:.2f} километров")
        print(f"На {day}-й день спортсмен достигнет результата не менее {totalDistance} километров.")