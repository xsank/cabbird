def addDigits(num):
    while num/10:
        t=num
        num=0
        while t:
            num+=t%10
            t/=10
    return num
      
    
if __name__=="__main__":
    print addDigits(38)
    print addDigits(540)