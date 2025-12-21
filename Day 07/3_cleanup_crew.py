num1 = 10
num2 = 20
try:
    res = num1/num2
    print(res)
except:
    print("Can not divide by zero")
finally:
    print("Execution Complete")