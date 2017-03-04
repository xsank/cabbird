import collections


def _findTargetSumWays(nums, S):
    return findAll(nums,S,0)


def findAll(nums,s,n):
    if len(nums)==1:
        if s==0:
            return 2 if nums[0]==s else 0
        else:
            return 1 if nums[0]==s or nums[0]==-s else 0
    else:
        return findAll(nums[:-1],s-nums[-1],n+1)+findAll(nums[:-1],s+nums[-1],n+1)


def findTargetSumWays(nums,S):
    length=len(nums)
    dp=[collections.defaultdict(int) for _ in range(length+1)]
    dp[0][0]=1
    for i in range(length):
        for j in dp[i]:
            dp[i+1][j+nums[i]]+=dp[i][j]
            dp[i+1][j-nums[i]]+=dp[i][j]
    return dp[length][S]


if __name__=="__main__":
    print findTargetSumWays([1,1,1,1,1],3)
    print findTargetSumWays([1],1)
    print findTargetSumWays([1],2)
    print findTargetSumWays([0,0,0,0,0,0,0,0,1],1)
