from structure.treenode import *


def isSymmetric(root):
    if not root:
        return True
    return compare(root.left,root.right)


def compare(left,right):
    if not left and not right:
        return True
    elif left and right:
        if left.val==right.val:
            return compare(left.left,right.right) and compare(left.right,right.left)
    return False

if __name__=="__main__":
    node=listToTree([1,2,2,None,3,None,3])
    print isSymmetric(node)
