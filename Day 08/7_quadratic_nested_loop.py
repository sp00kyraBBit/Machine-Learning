lst1 = list(range(100))
lst2 = list(range(1,100,2))

dup = []
for i in lst1:
    for j in lst2:
        if i==j:
            dup.append(i)

print("Duplicate Values: ",dup)