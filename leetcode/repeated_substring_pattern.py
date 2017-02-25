def repeatedSubstringPattern(str):
    length=len(str)
    for i in range(2,length+1):
        size=length/i
        if size*i==length:
            indexes=[j*size for j in range(i)]
            count=0
            leni=len(indexes)
            while count<size:
                ts=1
                for j in range(leni-1):
                    if str[indexes[j]+count]==str[indexes[j+1]+count]:
                        ts+=1
                    else:
                        break
                if ts<leni:
                    break
                count+=1
            if count==size:
                return True
    return False


if __name__=="__main__":
    print repeatedSubstringPattern("abab")
    print repeatedSubstringPattern("aba")
    print repeatedSubstringPattern("abac")
    print repeatedSubstringPattern("abcabcabcabc")
