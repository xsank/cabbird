def encode_space(string):
    list_s=[]
    for i in string:
        if i==' ':
            list_s.append("%20")
        else:
            list_s.append(i)
    return ''.join(list_s)


print encode_space('hello world')
