def _integerBreak(n):
    if n<=3:
        return n-1
    res=1
    while n>2:
        res*=3
        n-=3
    if n==1:
        res=res/3*(3+n)
    elif n==2:
        res*=n
    return res


def integerBreak(n):
    if n<=3:
        return n-1
    dp=[0]*(n+1)
    dp[2],dp[3]=2,3
    for i in range(4,n+1):
        dp[i]=max(2*dp[i-2],3*dp[i-3])
    return dp[n]


if __name__=="__main__":
    print integerBreak(2)
    print integerBreak(3)
    print integerBreak(4)
    print integerBreak(10)
    print integerBreak(16)
