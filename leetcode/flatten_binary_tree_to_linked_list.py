from structure.treenode import *


def flatten(root):
    


def modifyTree(root):
    if root:
        tleft=root.left
        tright=root.right
        if tleft:
            t=root.right
            root.right=root.left
            
            root.left.
        modifyTree(t)
        modifyTree(root.right)


if __name__=="__main__":
    root=listToTree([1,2,3,4,5,6])
    latten(root)
    printNode(root)
