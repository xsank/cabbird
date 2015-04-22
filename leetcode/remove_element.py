
def removeElement(A, elem):
    while elem in A:
        A.remove(elem)
    return len(A)


if __name__=="__main__":
    print removeElement([1,2,3,4,1],1)
