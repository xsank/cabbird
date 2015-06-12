import random

class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None


def listToTree(l):
    def addLeaf(root,node):
        if root:
            if root.left is None:
                root.left=node
            elif root.right is None:
                root.right=node
            else:
                if random.randint(0,1):
                    root=root.right
                else:
                    root=root.left
                addLeaf(root,node)
        else:
            root=node
        return root

    root=None
    _next=None
    for i in l:
        node=TreeNode(i)
        if root is None:
            root=node
        _next=addLeaf(_next,node)
    return root


def printNode(node):
    if node is not None:
        print node.val
        printNode(node.left)
        printNode(node.right)

