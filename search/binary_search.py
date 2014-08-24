
def binary_search(l=[],key=0):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)/2
        if l[mid]<key:
            low=mid+1
        elif l[mid]>key:
            high=mid-1
        else:
            return mid
    return -1

