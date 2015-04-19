
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None


def listToNode(l):
    head=None
    tail=None
    for i in l:
        node=ListNode(i)
        if head is None:
            head=node
        if tail is not None:
            tail.next=node
        tail=node
    return head

def printNode(node):
    while node is not None:
        print node.val
        node=node.next

