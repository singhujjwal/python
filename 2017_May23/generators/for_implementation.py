a = [10, 20, 30, 40, 50]


#for i in a: 
#    print i,


length = len(a)
iterator = iter(a)

while length:
    i = iterator.next()
    # Body of for loop
    print i,

    length -= 1

# -----------------------------

iterator = iter(a)

try:
    while True:
        i = iterator.next()
        # Body of 'for' loop
        print i,
except StopIteration: pass



