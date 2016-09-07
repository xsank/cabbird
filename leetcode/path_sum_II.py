from structure.treenode import *


def PathSum(root, sum):
    res=[]
    genPath(res,[],root,sum)
    return res


def genPath(total,path,root,_sum):
    if root:
        path.append(root.val)
        if not root.left and not root.right:
            if sum(path)==_sum:
                total.append(path)
        genPath(total,path[:],root.left,_sum)
        genPath(total,path[:],root.right,_sum)

    
if __name__=="__main__":
    node=listToTree([1,2,2,4,3,4,3])
    print PathSum(node,5)
    node=listToTree([1,2,2])
    print PathSum(node,3)
