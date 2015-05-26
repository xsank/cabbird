
def is_valid(res,n,target):
    return len(res)==n and sum(res)==target


def find_all_combinations(total,remain,res,n,target):
    if is_valid(res,n,target):
        total.append(res)
    if sum(res)>=target:
        return
    for i in remain:
        index=remain.index(i)+1
        rec=res[:]
        rec.append(i)
        remain=remain[index:]
        find_all_combinations(total,remain,rec,n,target)


def combinationSum3(k, n):
    total=[]
    if k>n or n>45:
        return total
    find_all_combinations(total,range(1,10),[],k,n)
    return total


if __name__=="__main__":
    print combinationSum3(3,9)

