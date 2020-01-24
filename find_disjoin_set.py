# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def merge_pair(pair1, pair2):
    if pair1[1] >= pair2[0] and pair1[1] <= pair2[1]:
        return (pair1[0], pair2[1])
    else:
        return (pair2[0], pair1[1])
        

def is_overlapping(pair1, pair2):
    if (pair1[1] >= pair2[0] and pair1[1] <= pair2[1]) or \
        (pair1[0] >= pair2[0] and pair1[1] <= pair2[1]) or \
        (pair1[1] >= pair2[0] and pair1[1] <= pair2[1]) or \
        (pair2[1] >=pair1[0] and pair2[0] <= pair1[1]):
        return True
    else:
        return False

def solution(A, B):
    # write your code in Python 3.6
    # 1. There wil be N intervals
    # 2. Find the overlapping intervals and reduce the intyervals by
    # creating unions
    
    pair_list = []
    union_list = []
    
    for i in range(len(A)):
        interval = (A[i], B[i])
        pair_list.append(interval)
    
    while pair_list:
        pair1 = pair_list.pop()
        for pair2 in pair_list:
            if is_overlapping(pair1, pair2):
                pair_list.remove(pair2)
                pair1 = merge_pair(pair1, pair2)
        union_list.append(pair1)
    return  len(union_list)