from structure.treenode import *


def levelOrder(root):
    queue=[root]
    res=[]
    cur_level=0
    while queue:
        node=queue.pop(0)
        if node:
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res


if __name__=="__main__":
    node=listToTree([1,2,2,4,3,4,3])
    printNode(node)
    print levelOrder(node)
