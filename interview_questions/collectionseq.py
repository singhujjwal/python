

from collections import deque

d = deque()

l = d.__len__()

print (f" The count is {d.count(0)}")


print (f" The length is {l}")

d.append(2)
d.append("singh")
for item in d:
    print (item)