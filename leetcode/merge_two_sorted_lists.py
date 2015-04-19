from structure.listnode import *

def mergeTwoLists(l1, l2):
    head=ListNode(-1)
    head.next=l1
    point=head
    while l1 and l2:
        if l1.val>l2.val:
            next=l2.next
            l2.next=point.next
            point.next=l2
            l2=next
        else:
            l1=l1.next
        point=point.next
    if l2:
        point.next=l2
    return head.next


if __name__=="__main__":
    l1=listToNode([2])
    l2=listToNode([1])
    printNode(mergeTwoLists(l1,l2))
