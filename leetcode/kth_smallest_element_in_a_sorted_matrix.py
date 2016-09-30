def kthSmallest(matrix, k):
    length=len(matrix)
    return matrix[(k-1)/length][(k-1)%length]


if __name__=="__main__":
    print kthSmallest([
       [ 1,  5,  9],
          [10, 11, 13],
             [12, 13, 15]
             ],8)
    print kthSmallest([
       [ 1,  5,  9],
          [10, 11, 13],
             [12, 13, 15]
             ],4)
    print kthSmallest([[1]],1)
