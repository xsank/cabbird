def minMoves(nums):
    return sum(nums)-len(nums)*min(nums)


if __name__=="__main__":
    print minMoves([1,2,3])
