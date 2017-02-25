def merge(nums1, m, nums2, n):
    k=m+n-1
    i=m-1
    j=n-1
    while k>=0:
        if i>=0 and j>=0:
            if nums1[i]>=nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
        else:
            if j>=0:
                nums1[k]=nums2[j]
                j-=1
        k-=1


if __name__=="__main__":
    print merge([0],0,[1],1)
    print merge([1],1,[0],0)
    print merge([1,3,4,0,0,0,0,0],3,[2,3,6,9],4)
    print merge([4,5,6,0,0,0],3,[1,2,3],3)
