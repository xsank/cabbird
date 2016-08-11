def isUgly(num):
    if num>0:
        while not num%2:
            num/=2
        while not num%3:
            num/=3
        while not num%5:
            num/=5
        return num==1
    return False
    
    
if __name__=="__main__":
    print isUgly(6)
    print isUgly(8)
    print isUgly(14)
    print isUgly(1)
    print isUgly(0)