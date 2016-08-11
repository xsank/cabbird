def nthUglyNumber(n):
    result=[1]
    index2=0
    index3=0
    index5=0
    for i in range(n-1):
        n2=result[index2]*2
        n3=result[index3]*3
        n5=result[index5]*5
        tmp=min(n2,n3,n5)
        if tmp==n2:
            index2+=1
        if tmp==n3:
            index3+=1
        if tmp==n5:
            index5+=1
        result.append(tmp)
    return result[-1]
        
    
    
if __name__=="__main__":
    print nthUglyNumber(6)
    print nthUglyNumber(8)
    print nthUglyNumber(2)
    print nthUglyNumber(1)
    print nthUglyNumber(10)
    print nthUglyNumber(11)