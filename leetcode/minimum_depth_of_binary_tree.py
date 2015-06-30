from structure.treenode import *

def minDepth(root):
    if root:
        if root.left is None:
            return minDepth(root.right)+1
        if root.right is None:
            return minDepth(root.left)+1
        return 1+min(minDepth(root.left),minDepth(root.right))
    return 0


if __name__=="__main__":
    root=listToTree([1,2,3,4,5,6])
    print minDepth(root)
