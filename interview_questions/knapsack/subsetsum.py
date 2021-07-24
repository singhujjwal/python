
# recursive subproblem 
# simple as fuck inspired by Aditya Verma 



from typing import List


def isSubsetSum(set, n, sum):
    if sum == 0:
        # empty subset will have a sum 0
        return True
    if n == 0:
        return False
    if set[n-1] > sum:
        return isSubsetSum(set,n-1, sum)
    return isSubsetSum(set, n-1, sum-set[n-1]) or isSubsetSum(set, n-1, sum)

def isSubsetSumN(arr, arr_len, sum):

    t= [[False for i in range(sum+1)] for j in range(arr_len+1)]

    # when sum = 0 there is a always an empty subset 
    for i in range(arr_len+1):
        t[i][0] = True
    
    # if the set is empty and sum is not zero a false case
    for j in range(1, sum+1):
        t[0][j] = False

    for i in range(arr_len+1):
        for j in range(sum+1):
            if j < arr[i-1]:
                t[i][j] = t[i-1][j]
            else:
                t[i][j] = t[i-1][j] or t[i-1][j-arr[i-1]]


    return t[n][sum]


if __name__ == '__main__':
    set = [3, 34, 4, 12, 5, 2]
    sum = 9
    n = len(set)
    # if (isSubsetSum(set, n, sum) == True):
    #     print("Found a subset with given sum")
    # else:
    #     print("No subset with given sum")

    if (isSubsetSumN(set, n, sum) == True):
        print("Found a subset with given sum")
    else:
        print("No subset with given sum")
    