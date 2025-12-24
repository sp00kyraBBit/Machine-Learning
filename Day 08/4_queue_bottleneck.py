lst = list(range(10))
print("Before pop: ",lst)
lst.pop()
print("After pop: ",lst)

from collections import deque
lst1 = deque(range(10))
print("Before pop: ",lst1)
lst1.pop()
print("After pop: ",lst1)
