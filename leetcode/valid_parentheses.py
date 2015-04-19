
def isValid(s):
    pair_dict={
        ')':'(',
        ']':'[',
        '}':'{'
    }
    stack=[]
    for c in s:
        if c=='}' or c==']' or c==')':
            if stack and stack[-1]==pair_dict[c]:
                stack.pop()
                continue
            else:
                return False
        stack.append(c)
    return not stack


if __name__=="__main__":
    print isValid("()[]{}")
    print isValid("([)]")

