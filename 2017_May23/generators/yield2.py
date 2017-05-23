def accumulate(initial_value=0):
    total = initial_value

    while True:
        v = yield
        print "Accumulating", v
        total += v
        yield total
        if v == 0: break

a = accumulate(0)
for i in a:
    num = input("Enter value: ")
    t = a.send(num)

print "Total accumulated:", t



#a = accumulate(0)
#a.next()
#t = a.send(10)
#print "Total = ", t

#a.next()
#t = a.send(20)
#print "Total = ", t

#a.next()
#t = a.send(0)


