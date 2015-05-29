
def canJump(nums):
    max_cover=0
    length=len(nums)
    for i in range(length):
        cover=nums[i]+i
        if cover>i and cover>=max_cover:
            max_cover=cover
        if max_cover<=i and i!=length-1:
            return False
    return True


if __name__=="__main__":
    print canJump([2,3,1,1,4])
    print canJump([3,2,1,0,4])
    print canJump([3])
    print canJump([0,2,3])
    print canJump([0])
    print canJump([2,0])
    print canJump([2,0,0])
    print canJump([1,1,1,0])
