from structure.treenode import *


def recursive(total,root):
    if root:
        if root.left and not root.left.left and not root.left.right:
            total.append(root.left.val)
        recursive(total,root.left)
        recursive(total,root.right)

def sumOfLeftLeaves(root):
    total=[]
    recursive(total,root)
    return sum(total)


if __name__=="__main__":
    _tree=listToTree([1,9,30,None,None,15,7])
    printNode(_tree)
    print sumOfLeftLeaves(_tree)
