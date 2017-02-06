def partition(s):
    total=[]
    search(s,[],total)
    return total


def search(s,res,total):
    if not s:
        total.append(res)
    for i in range(len(s)):
        if isPalindrome(s[:i+1]):
            t=res[:]
            t.append(s[:i+1])
            search(s[i+1:],t,total)
    

def isPalindrome(s):
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True


if __name__=="__main__":
    print partition("aa")
    print partition("aab")
    print partition("aabb")
