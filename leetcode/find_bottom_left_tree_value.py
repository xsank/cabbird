from structure.treenode import *


def largestValues(root):
    res=[0,root.val]
    dfs(root,0,res)
    return res[1]


def dfs(root,level,res):
    if root:
        if level>res[0]:
            res[0],res[1]=level,root.val
        dfs(root.left,level+1,res)
        dfs(root.right,level+1,res)
    

if __name__=="__main__":
    root=listToTree([1])
    printNode(root)
    print largestValues(root)
