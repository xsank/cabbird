from structure.listnode import *

def swapPairs(head):
    res_head=ListNode(-1)
    res_head.next=head
    p=res_head
    while p.next and p.next.next:
        even_p=p.next
        odd_p=even_p.next
        thr_p=odd_p.next
        p.next=odd_p
        p.next.next=even_p
        p.next.next.next=thr_p
        p=p.next.next
    return res_head.next


if __name__=="__main__":
    l=listToNode([1,2,3,4])
    printNode(swapPairs(l))
