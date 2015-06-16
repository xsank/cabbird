from structure.listnode import *

def deleteDuplicates(head):
    flag=1<<32
    _head=ListNode(-1)
    _head.next=head
    q=_head
    p=head
    repeat=False
    while p:
        if p.val!=flag:
            flag=p.val
            if repeat:
                q.next=p
                repeat=False
            else:
                if q.next!=p:
                    q=q.next
        else:
            repeat=True
        p=p.next
    if repeat:
        if q.next.val!=q.next.next.val:
            q.next.next=None
        else:
            q.next=None
    return _head.next


if __name__=="__main__":
    _list=listToNode([0,0,1,1,2,2,3,3,3,4,4,5,5])
    printNode(deleteDuplicates(_list))
