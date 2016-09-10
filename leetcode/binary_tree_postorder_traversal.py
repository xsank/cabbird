from structure.treenode import *


def postorderTraversal(root):
    res=[]
    postTravel(res,root)
    return res


def postTravel(res,root):
    if root:
        postTravel(res,root.left)
        postTravel(res,root.right)
        res.append(root.val)
    

if __name__=="__main__":
    root=listToTree([1,2,3])
    print postorderTraversal(root)
