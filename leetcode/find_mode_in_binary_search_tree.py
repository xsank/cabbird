from structure.treenode import *


def findMode(root):
    res=[]
    if root:
        cmap={}
        count(cmap,root)
        maxv=max(cmap.values())
        for k in cmap.keys():
            if cmap[k]==maxv:
                res.append(k)
    return res


def count(cmap,root):
    if root:
        if root.val in cmap:
            cmap[root.val]+=1
        else:
            cmap[root.val]=1
        if root.left:
            count(cmap,root.left)
        if root.right:
            count(cmap,root.right)


if __name__=="__main__":
    root=listToTree([1,None,2,2])
    print findMode(root)
