def grayCode(n):
    return [((i>>1)^i) for i in xrange(2 ** n)]


 
if __name__=="__main__":
    print grayCode(2)
