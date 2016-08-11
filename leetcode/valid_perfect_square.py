def isPerfectSquare(num):
    magic=1
    while num>0:
       num-=magic
       magic+=2
    return num==0
    
    
if __name__=="__main__":
    print isPerfectSquare(14)
    print isPerfectSquare(16)
    print isPerfectSquare(1)
    print isPerfectSquare(4)
    print isPerfectSquare(2147483647)