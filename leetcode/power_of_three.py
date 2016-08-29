import math


def isPowerOfThree(n):
    return n>0 and pow(3,round(math.log(n,3)))==n
    

if __name__=="__main__":
    print isPowerOfThree(0)
    print isPowerOfThree(6)
    print isPowerOfThree(9)
    print isPowerOfThree(243)
