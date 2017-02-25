def findDuplicates(nums):
    res=[]
    for i,n in enumerate(nums):
        absn=abs(n)
        if nums[absn-1]<0:
            res.append(absn)
        else:
            nums[absn-1]*=-1
    return res


if __name__=="__main__":
    print findDuplicates([4,3,2,7,8,2,3,1])
