def isPowerOfTwo(n):
    return n>0 and not n&(n-1)


if __name__=="__main__":
    print isPowerOfTwo(8)
    print isPowerOfTwo(0)
    print isPowerOfTwo(6)
