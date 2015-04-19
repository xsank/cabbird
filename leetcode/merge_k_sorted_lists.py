from structure.listnode import *

def mergeList(lists,l,r):
    if l<r:
        m=(l+r)/2
        l_list=mergeList(lists,l,m)
        r_list=mergeList(lists,m+1,r)
        return mergeTwoLists(l_list,r_list)
    else:
        return lists[l]


def mergeKLists(lists):
    if not lists:
        return None
    return mergeList(lists,0,len(lists)-1)

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
    l3=listToNode([3])
    printNode(mergeKLists([l1,l2,l3]))
