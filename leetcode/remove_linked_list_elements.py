from structure.listnode import *

def removeElements(head, val):
    _head=p=ListNode(-1)
    p.next=head
    while p:
        while p.next and p.next.val==val:
            p.next=p.next.next
        p=p.next
    return _head.next


if __name__=="__main__":
    _list=listToNode([])
    printNode(removeElements(_list,6))
