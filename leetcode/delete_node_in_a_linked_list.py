from structure.listnode import *


def deleteNode(node):
    node.val=node.next.val
    node.next=node.next.next


if __name__=="__main__":
    head=listToNode([1,2,3,4])
    printNode(head)
    deleteNode(head.next.next)
    printNode(head)
