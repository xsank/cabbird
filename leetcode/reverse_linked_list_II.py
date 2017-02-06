from structure.listnode import *


def reverseBetween(head,m,n):
    p=ListNode(-1)
    p.next=head
    for _ in range(m-1):
        p=p.next
    _head=p
    p=p.next
    pp=p
    t=n-m
    while t>0:
        ttp=p.next.next
        tp=p.next
        p.next.next=p
        p=tp
    _head.next=p
    return _head.next

if __name__=="__main__":
    _list=listToNode([1,2,3,4,5])
    printNode(reverseBetween(_list,2,4))
