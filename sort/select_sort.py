
def select_sort(l=[]):
    length=len(l)
    if length>1:
        for i in range(length-1):
            index=i
            for j in range(i+1,length):
                if l[index]>l[j]:
                    index=j
            if index!=i:
                l[index],l[i]=l[i],l[index]
    return l

