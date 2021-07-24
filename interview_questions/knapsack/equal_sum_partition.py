

def isSubsetSum(set, n, sum):
    if sum == 0:
        # empty subset will have a sum 0
        return True
    if n == 0:
        return False
    if set[n-1] > sum:
        return isSubsetSum(set,n-1, sum)
    return isSubsetSum(set, n-1, sum-set[n-1]) or isSubsetSum(set, n-1, sum)


def equal_sum_partition(arr, arr_len):
    arr_sum = sum(arr)
    if arr_sum %2 != 0:
        return False
    if arr_sum == 0:
        return True # two empty subsets
    arr_sum = int(arr_sum/2)
    print (arr_sum)
    return isSubsetSum(arr, arr_len, arr_sum)
    

if __name__ == '__main__':
    arr = [1,5,11,5,2,6]
    arr_len = len(arr)
    if equal_sum_partition(arr, arr_len):
        print ("Yes")
    else:
        print ("No")



    