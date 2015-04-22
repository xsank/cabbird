
def removeDuplicates(A):
    length=len(A)
    if length<=1:
        return length
    index=0
    for i in xrange(length):
        if A[index]!=A[i]:
            index+=1
            A[index]=A[i]
    return index+1


if __name__=="__main__":
    print removeDuplicates([1,2,3])
