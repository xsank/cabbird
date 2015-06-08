EVENT={'digit':0,'.':1,'e':2,'flag':3}

CONVERT_GRAPH=(
    (1,2,-1,3),
    (1,2,4,-1),
    (5,-1,-1,-1),
    (6,-1,-1,-1),
    (7,-1,-1,8),
    (5,-1,4,-1),
    (6,2,4,-1),
    (7,-1,-1,-1),
    (8,-1,-1,-1)
)

RESULT=(1,5,6,7,8)

def isNumber(s):
    good_s=''.join(s.split())
    state=0
    if good_s:
        for c in good_s:
            if c.isdigit():
                state=CONVERT_GRAPH[state][EVENT['digit']]
            elif c=='.':
                state=CONVERT_GRAPH[state][EVENT['.']]
            elif c=='e' or c=='E':
                state=CONVERT_GRAPH[state][EVENT['e']]
            elif c=='+' or c=='-':
                state=CONVERT_GRAPH[state][EVENT['flag']]
            else:
                state=-1
            if state==-1:
                break
    return state in RESULT


if __name__=="__main__":
    print isNumber("0")
    print isNumber(" 0.1 ")
    print isNumber("abc")
    print isNumber(".3")
    print isNumber("1 a")
    print isNumber("2e10")
    print isNumber("2e+10")
    print isNumber("+2e10")
    print isNumber("+2e.1")
