def _wrong_minimumTotal(triangle):
    length=len(triangle)
    if length==0 or len(triangle[0])==0:
        return 0
    dp=[0]*length
    dp[0]=triangle[0][0]
    for i in range(1,length):
        dp[i]=dp[i-1]+min(triangle[i])
    return dp[-1]


def minimumTotal(triangle):
    length=len(triangle)
    if length==0 or len(triangle[0])==0:
        return 0
    dp=[[0]*i for i in range(1,length+1)]
    dp[0][0]=triangle[0][0]
    for i in range(1,length):
        for j in range(i+1):
            dp[i][j]=triangle[i][j]+min(dp[i-1][max(0,j-1)],dp[i-1][min(j,i-1)])
    return min(dp[length-1])


if __name__=="__main__":
    print minimumTotal([
         [2],
             [3,4],
                [6,5,7],
                  [4,1,8,3]
                  ])
    print minimumTotal([[-1],[2,3],[1,-1,-3]])
