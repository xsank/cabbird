def reverse_cstring(cstring):
    res=list(cstring)
    left,right=0,len(cstring)-2
    while left<right:
        res[left],res[right]=res[right],res[left]
        left+=1
        right-=1
    return ''.join(res)


print reverse_cstring('hello$')
print reverse_cstring('$')
