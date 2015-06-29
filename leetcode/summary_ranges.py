
def summaryRanges(nums):
    length=len(nums)
    if length==0:
        return nums
    if length==1:
        return [str(nums[0])]
    start=end=-1
    res=[]
    for i in range(length-1):
        if start==-1:
            start=end=i
        if nums[i]+1==nums[i+1]:
            end+=1
        else:
            if end==start:
                res.append(str(nums[start]))
            else:
                res.append(str(nums[start])+"->"+str(nums[end]))
            start=end=-1
    if start==-1:
        res.append(str(nums[length-1]))
    else:
        res.append(str(nums[start])+"->"+str(nums[end]))
    return res

if __name__=="__main__":
    l=[0,1,2,4,5,6]
    print summaryRanges(l)
