from structure.listnode import *


def isPalindrome(head):
    if not head or not head.next:
        return True
    fast_p=slow_p=head
    while fast_p.next and fast_p.next.next:
        fast_p=fast_p.next.next
        slow_p=slow_p.next
    sec_p=slow_p.next
    slow_p.next=None
    while sec_p.next:
        t=sec_p.next
        sec_p.next=slow_p
        slow_p=sec_p
        sec_p=t
    sec_p.next=slow_p
    slow_p=head
    while sec_p.next:
        if slow_p.val != sec_p.val:
            return False
        sec_p=sec_p.next
        slow_p=slow_p.next
    return True


if __name__=="__main__":
    node=listToNode([1,2,3])
    print isPalindrome(node)
    node=listToNode([1,2,3,2])
    print isPalindrome(node)
    node=listToNode([1,2,3,3,2,1])
    print isPalindrome(node)
    node=listToNode([1,1,2,1])
    print isPalindrome(node)
    node=listToNode([1])
    print isPalindrome(node)
