from structure.listnode import *


def detectCycle(head):
    fast_p=slow_p=head
    while fast_p and fast_p.next and fast_p.next.next:
        fast_p=fast_p.next.next
        slow_p=slow_p.next
        if fast_p == slow_p:
            fast_p=head
            while slow_p != fast_p:
                slow_p=slow_p.next
                fast_p=fast_p.next
            return slow_p
    return None
    

if __name__=="__main__":
    head=listToNode([1,2,4,3,5,6])
    print detectCycle(head)
