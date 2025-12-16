# problem with determing equality of floatig point number
print(0.1 + 0.2 == 0.3)

# one of the fix is to round it up to a certain value then compare
print(round(0.1+0.2,1) == round(0.3,1))
