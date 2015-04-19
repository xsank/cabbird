
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

def merge(l1,l2):
    if l1==None:
        return l2
    if l2==None:
        return l1

    if l1.val<l2.val:
        p
    while l1 and l2:


def sortList(head):
    if head==None or head.next==None:
        return head
    i_node=head
    j_node=head.next


if __name__=="__main__":
    l=listToNode([1,3,5,2,4,6])
    printNode(sortList(l))

