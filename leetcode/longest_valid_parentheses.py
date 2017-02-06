
def longestValidParentheses(s):
    stack=[]
    maxlen=0
    last=-1
    for i,c in enumerate(s):
        if c=="(":
            stack.append(i)
        else:
            if not stack:
                last=i
            else:
                stack.pop()
                if not stack:
                    maxlen=max(maxlen,i-last)
                else:
                    maxlen=max(maxlen,i-stack[-1])
    return maxlen


if __name__=="__main__":
    print longestValidParentheses("(()")
    print longestValidParentheses(")()())")
    print longestValidParentheses("(())(")
    print longestValidParentheses("()(()")
