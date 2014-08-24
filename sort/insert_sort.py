
def insert_sort(l=[]):
    length=len(l)
    if length>1:
        for i in range(1,length):
            key=l[i]
            j=i-1
            while j>=0 and l[j]>key:
                l[j+1]=l[j]
                j-=1
            l[j+1]=key
    return l

