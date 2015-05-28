
def findAllCombinations(total,remain,res,target):
    _sum=sum(res)
    if _sum==target:
        total.append(res)
    if _sum>=target:
        return
    for i in remain:
        index=remain.index(i)
        rec=res[:]
        rec.append(i)
        findAllCombinations(total,remain[index:],rec,target)

def combinationSum(candidates, target):
    total=[]
    good_cand=sorted(candidates)
    findAllCombinations(total,good_cand,[],target)
    return total


if __name__=="__main__":
    print combinationSum([1,2,3,6,7],7)
