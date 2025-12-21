raw_age = input("Enter your age: ")
try:
    age = int(raw_age)
    print(f"Your age is {age}")
except ValueError:
    print("Numbers only")
