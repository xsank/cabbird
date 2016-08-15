def isBadVersion(version):
    return version>=1702766719

def firstBadVersion(n):
    left=1
    right=n
    while left<right:
        middle=(left+right)/2
        if isBadVersion(middle):
            right=middle
        else:
            left=middle+1
    return left
            
            
if __name__=="__main__":
    print firstBadVersion(2126753390)
        