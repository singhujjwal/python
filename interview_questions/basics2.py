


a = []
a.append(1)
print (a)
a.clear()
print (a)

a = list('Ujjwal')
print (a)
print (a.index('j'))
a.remove('j')

print (a)

b = a.copy()
print (b)
print (f"id of a is {id(a)}")
print (f"id of b is {id(b)}")

c= a
print (f"id of c is {id(c)} this is same as a because this is not a deep copy by calling the copy functions")

# function soreted returns a sorted version but doesnt do an inplace sorting 
print (sorted(a))
print (a)
# sort does a inplace sort of the list in alphabetical order or numerical order, Uppercase first
a.sort()
print (f"id of a is {id(a)}")
print (a)

# remove function removes an element exact search
a.remove('a')
print (a)
# pop pops at an index and removes it from the list as well 
print (a.pop(1))
print (a)

# insert at an index and shifts elements
a.insert(1, 'K')
print (a)
# clears the list
a.clear()
print (a)
b.reverse()
print (b)