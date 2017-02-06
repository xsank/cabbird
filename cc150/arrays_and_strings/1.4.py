from collections import Counter

def is_anagrams(str1,str2):
    return Counter(str1)==Counter(str2)


print is_anagrams("abc","cba")
print is_anagrams("abb","cba")
