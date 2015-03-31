
def longestPalindrome(s):

    def palindrome(s,i,j):
        while i>=0 and j<len(s) and s[j]==s[i]:
            i-=1
            j+=1
        return s[i+1:j]

    length=len(s)
    if length<=1:
        return s
    res=s[0]
    for i in range(length):
        tmp=""
        odd_s=palindrome(s,i,i)
        even_s=palindrome(s,i,i+1)
        odd_s_len=len(odd_s)
        even_s_len=len(even_s)
        if odd_s_len>even_s_len:
            tmp=odd_s
        else:
            tmp=even_s
        if len(tmp)>len(res):
            res=tmp
    return res


if __name__=="__main__":
    print longestPalindrome("aaaaaaaa")
    print longestPalindrome("aaabac")
    print longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth")


