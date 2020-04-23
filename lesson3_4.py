def my_func(x, y):
    result = 1 / (x ** abs(y))
    print(f"Result = {result}")
    return


my_func(int(input("Enter number 1: ")), int(input("Enter number 2: ")))
