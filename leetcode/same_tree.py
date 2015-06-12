from structure.treenode import *

def preorder(p,q):
    if p and q:
        if p.val==q.val:
            left=preorder(p.left,q.left)
            right=preorder(p.right,q.right)
            return left and right
        else:
            return False
    elif p or q:
        return False
    return True

def isSameTree(p, q):
   return preorder(p,q)

if __name__=="__main__":
    p=listToTree([1,2,3,4])
    q=listToTree([1,2,3,4])
    print isSameTree(p,p)
    p=listToTree([1,2,3,4])
    q=listToTree([1,2,3,4,5])
    print isSameTree(p,q)
    p=listToTree([1,2,3,4])
    q=listToTree([1,2,3,3])
    print isSameTree(p,q)
    p=listToTree([1])
    q=listToTree([])
    print isSameTree(p,q)
    p=listToTree([])
    q=listToTree([])
    print isSameTree(p,q)
