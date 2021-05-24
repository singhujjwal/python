#!/usr/bin/python3
# 
# # yield example
# yield applies to the generators and is now used to do async programming as well.

def test_yield(some_list):
    for i in some_list:
        if i%2 == 0:
            yield i

# Normal list iterator

mylist = [x*x for x in range(3)]
for i in mylist:
    print (i)

for i in mylist:
    print (i)
for i in mylist:
    print (i)
# now this is generator
iter_list = (x*x for x in range(3))


for i in iter_list:
    print (i)

for i in iter_list:
    print (i)


# if __name__ == "__main__":
#     print ("this is the main function...")
#     test_list = [1,2,3,4,5,6,7,8,10,12]
#     evens = test_yield(test_list)
#     for i in evens:
#         print (i)
