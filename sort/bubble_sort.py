
def bubble_sort(l=[]):
    length=len(l)
    if length>1:
        for i in range(length-1):
            for j in range(length-i-1):
                if l[j]>l[j+1]:
                    l[j],l[j+1]=l[j+1],l[j]
    return l

