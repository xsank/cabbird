
def lengthOfLongestSubstring(s):
    _max=1
    tmp_max=1
    index=0
    s_len=len(s)
    if s_len<=1:
        return s_len
    for i in range(1,s_len):
        tmp_count=0
        for j in range(index,i):
            if s[i]==s[j]:
                index=j+1
                if tmp_max>_max:
                    _max=tmp_max
                tmp_max=i-j
                break
            else:
                tmp_count+=1
                if tmp_count==i-index:
                    tmp_max+=1
    if tmp_max>_max:
        _max=tmp_max
    return _max


if __name__=="__main__":
    print lengthOfLongestSubstring("abcddcbae")
