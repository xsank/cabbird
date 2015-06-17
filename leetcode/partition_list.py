
from structure.listnode import *

def partition(head, x):
    left=right=None
    hleft=hright=None
    p=head
    while p:
        if not left:
            if p.val<x:
                hleft=left=p
        else:
            if p.val<x:
                left.next=p
                left=left.next
        if not right:
            if p.val>=x:
                hright=right=p
        else:
            if p.val>=x:
                right.next=p
                right=right.next
        p=p.next
    if hleft:
        left.next=hright
    if hright:
        right.next=None
    _head=hleft or hright
    return _head


if __name__=="__main__":
    _list=listToNode([1,2,3,4,5])
    printNode(partition(_list,3))
