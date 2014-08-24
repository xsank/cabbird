
def quick_sort(l=[]):
    length=len(l)
    if length>1:
        key=l[0]
        return quick_sort([i for i in l[1:] if i<= key])+[key]+quick_sort([i for i in l[1:] if i > key])
    else:
        return l
