def countNumbersWithUniqueDigits(n):
    if n==0:
        return 1
    if n==1:
        return 10
    if n==2:
        return 91
    total=91
    for i in range(n-2):
        t=81
        for j in range(8-i,9):
            t*=j
        total+=t
    return total
        
    
if __name__=="__main__":
    print countNumbersWithUniqueDigits(2)
    print countNumbersWithUniqueDigits(3)
    print countNumbersWithUniqueDigits(4)
