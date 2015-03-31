
def findMedianSortedArrays(A,B):
    C=[]
    while A and B:
        if A[0]<=B[0]:
            C.append(A.pop(0))
        else:
            C.append(B.pop(0))
    T=A or B
    C.extend(T)
    length=len(C)
    if length&1:
        return C[length>>1]
    else:
        return ((C[length>>1]+C[(length>>1)-1])/2.0)


if __name__=="__main__":
    print findMedianSortedArrays([1,2,3],[4,5])
