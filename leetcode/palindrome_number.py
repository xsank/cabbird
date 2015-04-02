
def isPalindrome(x):
    if x<0:
        return False
    s_x=str(x)
    length=len(s_x)
    if length==1:
        return True
    head=0
    tail=length-1
    while head<tail and s_x[head]==s_x[tail]:
        head+=1
        tail-=1
    return True if head>=tail else False


if __name__=="__main__":
    print isPalindrome(121)
    print isPalindrome(1221)
    print isPalindrome(11)
    print isPalindrome(-1)
    print isPalindrome(1)
    print isPalindrome(12)
