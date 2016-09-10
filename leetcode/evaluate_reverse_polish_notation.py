import operator


def _evalRPN(tokens):
    num_stack=[]
    for i in tokens:
        if i.lstrip("-").isdigit():
            num_stack.append(i)
        else:
            a=num_stack.pop()
            b=num_stack.pop()
            if i=="/" and int(a)*int(b)<0:
                num_stack.append(str(-eval(''.join(["-",b,i,a]))))
            else:
                num_stack.append(str(eval(''.join([b,i,a]))))
    return int(num_stack[0])


def evalRPN(tokens):
    num_stack=[]
    op_map={
        "+":operator.add,
        "-":operator.sub,
        "*":operator.mul,
        "/":operator.div
    }
    for i in tokens:
        if i.lstrip("-").isdigit():
            num_stack.append(int(i))
        else:
            a=num_stack.pop()
            b=num_stack.pop()
            if i=="/" and a*b<0:
                num_stack.append(-op_map[i](-b,a))
            else:
                num_stack.append(op_map[i](b,a))
    return num_stack[0]


if __name__=="__main__":
    print evalRPN(["2", "1", "+", "3", "*"])
    print evalRPN(["4", "13", "5", "/", "+"])
    print evalRPN(["3","-4","+"])
    print evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    print evalRPN(["4","-2","/","2","-3","-","-"])
