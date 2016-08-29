def majorityElement(nums):
    dic={}
    for i in nums:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    limit=len(nums)/3
    res=[k for k in dic if dic[k]>limit]
    return res


if __name__=="__main__":
    print majorityElement([3,3,3,2,2,1])
    print majorityElement([])
