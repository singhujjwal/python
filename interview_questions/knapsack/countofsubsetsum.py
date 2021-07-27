

def countofsubsetsumM(arr, arr_len, sum):
    if sum == 0:
        return 1
    t = [[0 for j in range(sum+1)] for i in range(arr_len+1)]


    # initialize
    # when arr element is null no answer is correct
    for j in range(sum+1):
        t[0][j] = 0
    for i in range(0, arr_len+1):
        t[i][0] = 1

    print (t)

    for i in range(1, arr_len+1):
        for j in range(1, sum+1):
            if arr[i-1] > j:
                t[i][j] = t[i-1][j]
            else:
                t[i][j] = t[i-1][j] + t[i-1][j-arr[i-1]]

    print (t)    
    print (t[arr_len][sum])



arr = [1, 2, 3, 3]
sum = 6 

countofsubsetsumM(arr,4,6)




