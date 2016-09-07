from structure.treenode import *


def levelOrder(root):
    res=[]
    levelTravel(res,root,0)
    res.reverse()
    return res


def levelTravel(total,root,level):
    if root:
        if len(total)==level:
            total.append([])
        total[level].append(root.val)
        levelTravel(total,root.left,level+1)
        levelTravel(total,root.right,level+1)

    
if __name__=="__main__":
    node=listToTree([1,2,2,4,3,4,3])
    print levelOrder(node)
