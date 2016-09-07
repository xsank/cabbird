from structure.treenode import *


def binaryTreePaths(root):
    res=[]
    genTreePaths(res,[],root)
    return res


def genTreePaths(res,tl,root):
    if root:
        tl.append(root.val)
        if not root.left and not root.right:
            res.append('->'.join(map(str,tl)))
        genTreePaths(res,tl[:],root.left)
        genTreePaths(res,tl[:],root.right)


if __name__=="__main__":
    root=listToTree([1,2,3,4])
    print binaryTreePaths(root)
