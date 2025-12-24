s = "test"
for _ in range(10000):
    s += "a"
print(s)

# fix
s = "text"
for _ in range(10000):
    s = "".join("a")
print(s)