def reverseWords(s):
    _list=s.split()
    _list.reverse()
    return ' '.join(_list)
    
   
if __name__=="__main__":
    print reverseWords("the sky is blue")