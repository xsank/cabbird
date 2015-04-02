
def rotate(nums,k):
    length=len(nums)
    k=k%length
    if k!=0:
        _nums=nums[length-k:]+nums[:length-k]
        nums=_nums[:]


if __name__=="__main__":
    rotate([1,2,3,4,5,6,7],10)
    rotate([1,2],1)
    rotate([1,2,3],1)
    rotate([1],0)
