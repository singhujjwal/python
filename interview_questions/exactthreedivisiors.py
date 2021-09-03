
import pdb

def isThree(n: int) -> bool:
    # every number greater than 3 has two divisors 1 and the number, if there exists another number than true else false
    if n <=3:
        return False
    isthreediv = False
    pdb.set_trace()
    for i in range(2, int(n/2)+1):
        if n%i == 0:
            if isthreediv == False:
                isthreediv = True
            else:
                return False
    if isthreediv:
        return True
    return False


print (isThree(4))
            