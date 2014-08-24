MAX_RANGE=100

def count_sort(l=[]):
    length=len(l)
    if length>1:
        tmp=[0 for i in range(length)]
        bucket=[0 for i in range(MAX_RANGE)]
        for i in l:
            bucket[i]+=1
        for i in range(1,len(bucket)):
            bucket[i]=bucket[i-1]+bucket[i]
        for i in l:
            tmp[bucket[i]-1]=i
            bucket[i]-=1
        l=tmp
    return l
