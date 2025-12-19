lst = list(range(-500000,500000))
set_lst = set(lst)
for i in lst:
    if i == -1:
        print("Element found")
        break

if -1 in set_lst:
    print("Element found")
else:
    print("Element not found")