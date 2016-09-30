def decodeString(s):
    num_stack=[]
    c_stack=[]
    t_num=[]
    for i in s:
        if i.isdigit():
            t_num.append(i)
        elif i=="[":
            num_stack.append(int(''.join(t_num)))
            t_num=[]
            c_stack.append(i)
        elif i.isalpha():
            c_stack.append(i)
        else:
            ts=[]
            while c_stack[-1]!="[":
                ts.insert(0,c_stack.pop())
            c_stack.pop()
            c_stack.append(''.join(ts)*num_stack.pop())
    return ''.join(c_stack)


if __name__=="__main__":
    print decodeString("3[a]2[bc]")
    print decodeString("3[a2[c]]")
    print decodeString("2[abc]3[cd]ef")
    print decodeString("100[leetcode]")
