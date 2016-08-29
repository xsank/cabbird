from structure.listnode import *


def oddEvenList(head):
    if not head:
        return None
    even_head=head
    todd_head=odd_head=head.next
    while todd_head and todd_head.next:
        even_head.next=todd_head.next
        even_head=even_head.next
        todd_head.next=even_head.next
        todd_head=todd_head.next
    even_head.next=odd_head
    return head


if __name__=="__main__":
    head=listToNode([1,2,3,4,5,6])
    oddEvenList(head)
    printNode(head)
