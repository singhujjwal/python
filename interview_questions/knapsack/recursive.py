
# recursive subproblem 
# simple as fuck inspired by Aditya Verma 



from typing import List

def knapSack(W: int, wt: List, val: List, num_of_elem: int):
    if W == 0 or num_of_elem == 0:
        return 0
    # if the weight of last element is less than or equal to total weight
    if wt[num_of_elem-1] <= W:
        return max(val[num_of_elem-1]+knapSack(
            W-wt[num_of_elem-1], wt, val, num_of_elem-1),
            knapSack(W, wt, val, num_of_elem-1))
    else:
        return knapSack(W, wt, val, num_of_elem-1)


if __name__ == '__main__':
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    print (knapSack(W, wt, val, n))
    