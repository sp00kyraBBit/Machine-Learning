age = int(input("Enter Age: "))
if age < 0:
    raise ValueError("No negatives")
else:
    print(f"Your age is {age}")
