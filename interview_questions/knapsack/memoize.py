


from typing import List

def knapSack(W: int, wt: List, val: List, num_of_elem: int):
    if W == 0 or num_of_elem == 0:
        return 0


    # now figure out the problem space actually, what is the limit of numbers and what is the total weight
    # say W<=1000
    # num_of_elem<=100 so list of values and corresponding weights
    # Matrix made of changing variable
    
    t = [[-1 for i in range(W+1)] for j in range(num_of_elem+1)]

    print (t)

    # Initialize 
    for i in range(num_of_elem+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                t[i][j] = 0


    
    # row is the values
    # columns is the total weight of knapsack
    for i in range(1, (num_of_elem+1)):
        for j in range(1, (W+1)):
            if wt[i-1] <= W:
                t[i][j] = max(val[i-1]+t[i-1][j-wt[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][W]

    print (t)

    return t[num_of_elem][W]


if __name__ == '__main__':
    val = [60, 100, 120]
    wt = [1, 2, 3]
    W = 5
    n = len(val)
    print (knapSack(W, wt, val, n))