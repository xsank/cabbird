def lengthOfLIS(nums):
    length=len(nums)
    dp=[1 for i in range(length)]
    for i in range(length):
        for j in range(i):
            t=dp[j]+1
            if nums[i]>nums[j] and dp[i]<t:
                dp[i]=t
    return max(dp) if dp else 0
    
    
if __name__=="__main__":
    print lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
    print lengthOfLIS([])
    print lengthOfLIS([1])
    print lengthOfLIS([2,1])
    print lengthOfLIS([1,2,1])
    print lengthOfLIS([1,3,6,7,9,4,10,5,6])
    print lengthOfLIS([10,9,2,5,3,7,101,18])
    print lengthOfLIS([8,9,1,2,3])