from structure.listnode import *


def hasCycle(head):
    fast_p=slow_p=head
    while fast_p and fast_p.next and fast_p.next.next:
        fast_p=fast_p.next.next
        slow_p=slow_p.next
        if fast_p is slow_p:
            return True
    return False
    


if __name__=="__main__":
    head=listToNode([1,2,4,3,5,6])
    print hasCycle(head)
