def findAllCombinations(total,remain,result,n):
    if len(result)==n:
        total.append(result)
        return
    _set=[]
    for i in remain:
        if i not in _set:
            _set.append(i)
            index=remain.index(i)
            rem=remain[index+1:]
            res=result[:]
            res.append(i)
            findAllCombinations(total,rem,res,n)

def subsets(nums):
    total=[]
    nums=sorted(nums)
    length=len(nums)
    for n in range(length+1):
        findAllCombinations(total,nums,[],n)
    return total


if __name__=="__main__":
    print subsets([1])
    print subsets([4,1,0])
    print subsets([1,2,2])
