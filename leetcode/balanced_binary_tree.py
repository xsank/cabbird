from structure.treenode import *

def getHeight(root):
    return 0 if not root else 1+max(getHeight(root.left),getHeight(root.right))

def isBalanced(root):
    if root:
        if abs(getHeight(root.left)-getHeight(root.right))>1:
            return False
        return isBalanced(root.left) and isBalanced(root.right)
    return True


if __name__=="__main__":
    root=listToTree([1,2,3,4,5,6,7])
    print isBalanced(root)

