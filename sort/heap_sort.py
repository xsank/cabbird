
def heap_sort(l=[]):

    def sift_down(start,end):
        root=start
        while True:
            child=2*root+1
            if child>end:
                break
            if child+1<=end and l[child]<l[child+1]:
                child+=1
            if l[root]<l[child]:
                l[root],l[child]=l[child],l[root]
                root=child
            else:
                break

    length=len(l)
    if length>1:
        for start in range((length-2)/2,-1,-1):
            sift_down(start,length-1)

        for end in range(length-1,0,-1):
            l[0],l[end]=l[end],l[0]
            sift_down(0,end-1)
    return l

