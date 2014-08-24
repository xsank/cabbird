MAX_BIT=2

def radix_sort(l=[]):
    length=len(l)
    if length>1:
        for bit in range(MAX_BIT):
            bucket=[[] for i in range(10)]
            for i in l:
                bucket[i/(10**bit)%10].append(i)
            l=[i for item in bucket for i in item]
    return l
