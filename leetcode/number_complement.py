import math


def _findComplement(num):
    bit=1
    while bit<=num:
        bit<<=1
    return num^(bit-1)


def findComplement(num):
    return num^(2**(int(math.log(num,2))+1)-1)


if __name__=="__main__":
    print findComplement(5)
    print findComplement(1)
    print findComplement(4)
