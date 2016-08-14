def divide(dividend, divisor):
    if divisor==0:
        return 2147483647
    abs_dividend=abs(dividend)
    abs_divisor=abs(divisor)
    res=0
    while abs_dividend>abs_divisor:
        t=abs_divisor
        count=1
        while abs_dividend>(t<<1):
            t<<=1
            count<<=1
        res+=count
        abs_dividend-=t
    if abs_dividend==abs_divisor:
        res+=1
    if dividend * divisor<0:
        return -res
    else:
        return min(res,2147483647)
    
    
   
if __name__=="__main__":
    print divide(10,3)
    print divide(9,3)
    print divide(9,0)
    print divide(-2147483648,-1)
    print divide(9,-3)
    print divide(9,-4)