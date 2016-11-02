def is_rotation(str1,str2):
    return len(str1)==len(str2) and (str2+str2).find(str1)>-1


print is_rotation("waterbottle","erbottlewat")
print is_rotation("abc","bcd")
print is_rotation("","")
print is_rotation("a","")
