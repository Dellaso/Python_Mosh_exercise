try:
    age = int(input("age: "))
    income = 10000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0.")
except ValueError:
    print("Invalid value!")
