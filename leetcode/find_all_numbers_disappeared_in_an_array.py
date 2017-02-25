def findDisappearedNumbers(nums):
    res=[0]*len(nums)
    for i in nums:
        res[i-1]=1
    return [i+1 for i,n in enumerate(res) if n==0]


if __name__=="__main__":
    print findDisappearedNumbers([4,3,2,7,8,2,3,1])
