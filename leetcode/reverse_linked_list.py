from structure.listnode import *

def reverseList(head):
    _head=p=ListNode(-1)
    p=head
    while p:
        t=_head.next
        tt=p.next
        _head.next=p
        p.next=t
        p=tt
    return _head.next

if __name__=="__main__":
    _list=listToNode([1,2,3,4,5])
    printNode(reverseList(_list))
