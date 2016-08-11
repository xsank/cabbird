def canConstruct(ransomNote, magazine):
    mag_dict={}
    for c in magazine:
        if c in mag_dict:
            mag_dict[c]+=1
        else:
            mag_dict[c]=1
    for c in ransomNote:
        if c in mag_dict:
            mag_dict[c]-=1
            if mag_dict[c]<0:
                return False
        else:
            return False
    return True
    
    
if __name__=="__main__":
    print canConstruct("a", "b")
    print canConstruct("aa", "ab")
    print canConstruct("aa", "aab")