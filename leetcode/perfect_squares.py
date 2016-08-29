#you should use dp as class property to ac the problem!


def numSquares(n):
    dp={0:0}
    sqrt=int(pow(n,0.5))
    for i in xrange(n+1):
        for j in xrange(1,sqrt+1):
            ti=i+j*j
            tv=dp[i]+1
            if ti<=n and (ti not in dp or tv<dp[ti]):
                dp[ti]=tv
    return dp[n]


if __name__=="__main__":
    print numSquares(12)
    print numSquares(13)
    print numSquares(9975)
