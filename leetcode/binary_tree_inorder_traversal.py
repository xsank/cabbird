from structure.treenode import *

def recursive(total,root):
    if root:
        recursive(total,root.left)
        total.append(root.val)
        recursive(total,root.right)

def inorderTraversal(root):
    total=[]
    recursive(total,root)
    return total


if __name__=="__main__":
    _tree=listToTree([1,2,3])
    printNode(_tree)
    print inorderTraversal(_tree)
