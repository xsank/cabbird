from structure.listnode import *

def removeNthFromEnd(head, n):
    res=head
    slow_point=head
    fast_point=slow_point
    while n:
        fast_point=fast_point.next
        n-=1
    if fast_point is None:
        res=res.next
    else:
        while fast_point.next:
            slow_point=slow_point.next
            fast_point=fast_point.next
        slow_point.next=slow_point.next.next
    return res


if __name__=="__main__":
    l=listToNode([1,2,3,4,5])
    printNode(removeNthFromEnd(l,5))

