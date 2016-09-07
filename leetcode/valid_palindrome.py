def _isPalindrome(s):
    right=len(s)-1
    left=0
    while left<right:
        if not s[left].isalnum():
            left+=1
            continue
        if not s[right].isalnum():
            right-=1
            continue
        if s[left].lower()!=s[right].lower():
                return False
        else:
            left+=1
            right-=1
    return True


def isPalindrome(s):
    ns=[c.lower() for c in s if c.isalnum()]
    left=0
    right=len(ns)-1
    while left<right:
        if ns[left]!=ns[right]:
            return False
        left+=1
        right-=1
    return True


if __name__=="__main__":
    print isPalindrome("A man, a plan, a canal: Panama")
    print isPalindrome("race a car")
    print isPalindrome("")
