import math


def constructRectangle(area):
    sqrt=int(math.sqrt(area))
    if sqrt*sqrt==area:
        return [sqrt,sqrt]
    else:
        for i in range(sqrt,0,-1):
            if not area%i:
                return [area/i,i]


if __name__=="__main__":
    print constructRectangle(4)
    print constructRectangle(1)
    print constructRectangle(5)
