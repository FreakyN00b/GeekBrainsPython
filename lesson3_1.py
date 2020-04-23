def test(n_1, n_2):
    num = round(n_1 / n_2, 2)
    print(f"Result = {num}")


try:
    test(int(input("Enter number 1: ")), int(input("Enter number 2: ")))
except ZeroDivisionError:
    print("We can`t divide by zero!")
except ValueError:
    print("You`ve entered not a number!")

