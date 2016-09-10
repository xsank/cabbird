from structure.treenode import *


def preorderTraversal(root):
    res=[]
    preTravel(res,root)
    return res


def preTravel(res,root):
    if root:
        res.append(root.val)
        preTravel(res,root.left)
        preTravel(res,root.right)
    

if __name__=="__main__":
    root=listToTree([1,2,3])
    print preorderTraversal(root)
