from structure.treenode import *


def hasPathSum(root, sum):
    if not root:
        return False
    if not root.left and not root.right and root.val==sum:
        return True
    return hasPathSum(root.left,sum-root.val) or hasPathSum(root.right,sum-root.val)

    
if __name__=="__main__":
    node=listToTree([1,2,2,4,3,4,3])
    print hasPathSum(node,5)
    node=listToTree([1,2])
    print hasPathSum(node,1)
