n=6

def guess(num):
    return n-num

def guessNumber(n):
    if guess(n)==0:
        return n
    left=1
    right=n
    while left<right:
        middle=(left+right)/2
        if guess(middle)<0:
            right=middle
        elif guess(middle)>0:
            left=middle
        else:
            return middle
    return left
    
    
if __name__=="__main__":
    print guessNumber(10)