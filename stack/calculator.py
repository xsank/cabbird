import operator
from stack import Stack


class Calculator:
    def __init__(self):
        self.ops={'+':operator.add,
                  '-':operator.sub,
                  '*':operator.mul,
                  '/':operator.div}
        self.pri={'+':1,'-':1,'*':2,'/':2,'(':4,')':4}
        self.postfix=Stack()

    def infix_to_postfix(self,s):
        tmp=Stack()
        for i in s:
            if i.isdigit():
                self.postfix.push(i)
            elif i !=')':
                if tmp.is_empty():
                    tmp.push(i)
                else:
                    if self.pri[i]>self.pri[tmp.top()]:
                        tmp.push(i)
                    else:
                        while not tmp.is_empty():
                            t=tmp.top()
                            if t=='(':
                                break
                            self.postfix.push(tmp.pop())
                        tmp.push(i)
            else:
                t=tmp.pop()
                while t!='(':
                    self.postfix.push(t)
                    t=tmp.pop()
        while not tmp.is_empty():
            self.postfix.push(tmp.pop())

    def calculate(self,s):
        self.infix_to_postfix(s)
        self.cal_postfix()

    def cal_postfix(self):
        tmp=Stack()
        for i in self.postfix:
            if i.isdigit():
                tmp.push(i)
            else:
                right=tmp.pop()
                left=tmp.pop()
                tmp.push(self.ops[i](int(left),int(right)))
        print tmp.pop()

if __name__=="__main__":
    cal=Calculator()
    cal.calculate('1+((9-1)/2+(3-1)*3)*2+8/2')



