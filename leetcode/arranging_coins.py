import math


def _arrangeCoins(n):
    res=0
    while (1+res)*res/2<=n:
        res+=1
    return res-1


def arrangeCoins(n):
    return int(math.sqrt(2*n+0.25)-0.5)


if __name__=="__main__":
    print arrangeCoins(0)
    print arrangeCoins(1)
    print arrangeCoins(5)
    print arrangeCoins(6)
    print arrangeCoins(8)
