def minDistance(word1, word2):
    length1=len(word1)
    length2=len(word2)
    dp=[[0 for i in range(length2+1)] for j in range(length1+1)]
    for i in range(length1+1):
        dp[i][0]=i
    for j in range(length2+1):
        dp[0][j]=j
    for i in range(1,length1+1):
        for j in range(1,length2+1):
            if word1[i-1]==word2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)
    return dp[length1][length2]


if __name__=="__main__":
    print minDistance("hello","world")
    print minDistance("abc","cba")
    print minDistance("a","")
    print minDistance("","a")
    print minDistance("a","ab")
    print minDistance("ab","c")
