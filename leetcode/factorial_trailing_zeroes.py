#time limit exceeded
def _trailingZeroes(n):
    count=0
    while n>0:
        t=n%5
        if not t:
            count+=1
        else:
            n=n-t
        n-=5
    return count

def trailingZeroes(n):
    count=0
    while n:
        n/=5
        count+=n
    return count


if __name__=="__main__":
    print trailingZeroes(5)
    print trailingZeroes(4)
    print trailingZeroes(10)
    print trailingZeroes(1808548329)


