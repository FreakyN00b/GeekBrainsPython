def my_func (name, surname, city_born, date, city_living, email, phone):
    print(f" Your name is {name} {surname}. You were born in {city_born} in {date}. Nowadays you live in {city_living}. Your e-mail is {email} and your phone number is {phone}.")
    return

my_func(
    input("Enter your name: "),
    input("Enter your surname: "),
    input("Enter where you were born: "),
    input("Enter when you were born: "),
    input("Enter where do you live: "),
    input("Enter your email: "),
    input("Enter your phone number: "))
