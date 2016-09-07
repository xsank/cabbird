from structure.treenode import *


def maxDepth(root):
    if root:
        return max(maxDepth(root.left)+1,maxDepth(root.right)+1)
    else:
        return 0


if __name__=="__main__":
    root=listToTree([1,2,3,4,5,6])
    print maxDepth(root)
    root=listToTree([])
    print maxDepth(root)
