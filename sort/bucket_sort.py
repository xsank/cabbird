MAX_RANGE=100

def bucket_sort(l=[]):
    length=len(l)
    if length>1:
        bucket=[[] for i in range(MAX_RANGE)]
        for i in l:
            bucket[i].append(i)
        l=[]
        for item in bucket:
            while item:
                l.append(item.pop(0))
    return l
