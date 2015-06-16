def findAllCombinations(total,remain,result,n):
    if len(result)==n:
        total.append(result)
        return
    for i in remain:
        index=remain.index(i)
        rem=remain[index+1:]
        res=result[:]
        res.append(i)
        findAllCombinations(total,rem,res,n)

def combine(n, k):
    total=[]
    findAllCombinations(total,range(1,n+1),[],k)
    return total


if __name__=="__main__":
    print combine(4,2)
    print combine(4,4)
