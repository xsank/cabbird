def coinChange(coins, amount):
    if amount==0:
        return 0
    dp=[0]+[-1]*amount
    for i in range(1,amount+1):
        res=[dp[i-j]+1 for j in coins if i>=j and dp[i-j]!=-1]
        if res:
            dp[i]=min(res)
    return dp[amount]


if __name__=="__main__":
    print coinChange([1,2,5],11)
    print coinChange([2],3)
    print coinChange([],1)
    print coinChange([2],0)
    print coinChange([2],1)
    print coinChange([2147483647],2)
