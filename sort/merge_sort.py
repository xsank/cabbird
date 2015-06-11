
def merge_sort(l=[]):
    length=len(l)

    def merge(left,right):
        res=[]
        while left and right:
            res.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        while left:
            res.append(left.pop(0))
        while right:
            res.append(right.pop(0))
        return res

    if length<=1:
        return l
    else:
        middle=length/2
        return merge(merge_sort(l[:middle]),merge_sort(l[middle:]))

