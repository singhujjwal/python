def accumulate(total=0):
    while True:
        total += yield 
        yield total


nums = [0, 10, 20, 30, 40, 50, 60, 70]
acc = accumulate()

#for i in acc:
#    v = nums.pop()
#    if not v: break
#    print acc.send(v)

for n in nums:
    acc.next()
    print acc.send(n)
    
