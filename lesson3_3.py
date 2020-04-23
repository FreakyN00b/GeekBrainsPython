def my_func (a, b, c):
    nums = [a, b, c]
    i = min(nums)
    nums.remove(i)
    sum = nums[0] + nums[1]
    print(f"The summ of two the biggest numbers is {sum}.")
    return


my_func(int(input("Enter number one: ")),
        int(input("Enter number two: ")),
        int(input("Enter number three: ")))