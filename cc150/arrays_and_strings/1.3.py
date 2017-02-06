def remove_dumplicates(string):
    length=len(string)
    if length<2:
        return string
    else:
        list_s=list(string)
        tail=1
        for i in range(1,length):
            j=0
            while j<tail: 
                if list_s[i]==list_s[j]:
                    break
                j+=1
            if tail==j:
                list_s[tail]=list_s[i]
                tail+=1
    return ''.join(list_s[:tail])


print remove_dumplicates("")
print remove_dumplicates("a")
print remove_dumplicates("aa")
print remove_dumplicates("ab")
print remove_dumplicates("hello")
