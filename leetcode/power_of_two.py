def isPowerOfTwo(n):
    if n>0:
        count=0
        while n:
            n&=(n-1)
            count+=1
        return count==1
    else:
        return False
    
if __name__=="__main__":
    print isPowerOfTwo(8)
    print isPowerOfTwo(6)