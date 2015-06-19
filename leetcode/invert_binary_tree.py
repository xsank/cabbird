from structure.treenode import *

def invertTree(root):
    if root:
       t=root.left
       root.left=invertTree(root.right)
       root.right=invertTree(t)
    return root


if __name__=="__main__":
    _tree=listToTree([1,2,3,4,5])
    printNode(_tree)
    printNode(invertTree(_tree))
