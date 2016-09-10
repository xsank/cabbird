from structure.treenode import *


def sumNumbers(root):
    res=[0]
    genNum(res,0,root)
    return sum(res)


def genNum(res,s,root):
    if root:
        s*=10
        s+=root.val
        if root.left:
            genNum(res,s,root.left)
        if root.right:
            genNum(res,s,root.right)
        if not root.left and not root.right:
            res.append(s)


if __name__=="__main__":
    root=listToTree([1,2,3])
    print sumNumbers(root)
