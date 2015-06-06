
def climbStairs(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    a=1
    b=2
    for i in range(2,n):
        b=a+b
        a=b-a
    return b


if __name__=="__main__":
    print climbStairs(10)
    print climbStairs(1)
    print climbStairs(2)
