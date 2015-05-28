
def findAllCombinations(total,remain,res,target):
    _sum=sum(res)
    if _sum==target:
        total.append(res)
    if _sum>=target:
        return
    length=len(remain)
    for i in range(length):
        if i>0 and remain[i]==remain[i-1]:
            continue
        rem=remain[i+1:]
        rec=res[:]
        rec.append(remain[i])
        findAllCombinations(total,rem,rec,target)

def combinationSum2(candidates, target):
    total=[]
    good_cand=sorted(candidates)
    findAllCombinations(total,good_cand,[],target)
    return total


if __name__=="__main__":
    #print combinationSum2([23,29,8,24,5,7,25,29,18,18,32,29,30,5,9,23,27,15,28,32,11,24,11,29,12,32,5,7,31,16,7,19,10,33,8,10,5,21,26,18,26,23,5,21,24,31,31,8,11,16,5,17,5,33,34,12,31,26,7,27],22)
    print combinationSum2([10,1,2,7,6,1,5],8)
    print combinationSum2([1],1)

