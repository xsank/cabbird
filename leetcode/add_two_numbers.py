
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None


def listToNode(l):
    head=None
    tail=None
    for i in l:
        node=ListNode(i)
        if head is None:
            head=node
        if tail is not None:
            tail.next=node
        tail=node
    return head

def printNode(node):
    while node is not None:
        print node.val
        node=node.next


def addTwoNumbers(l1,l2):
    head=None
    tail=None
    carry=0
    while l1 is not None and l2 is not None:
        cur_val=(l1.val+l2.val+carry)%10
        tmp_carry=(l1.val+l2.val+carry)/10
        node=ListNode(cur_val)
        if head is None:
            head=node
        if tail is not None:
            tail.next=node
        tail=node
        carry=tmp_carry
        l1=l1.next
        l2=l2.next
    l=l1 or l2
    while l is not None:
        cur_val=(l.val+carry)%10
        tmp_carry=(l.val+carry)/10
        node=ListNode(cur_val)
        tail.next=node
        tail=node
        carry=tmp_carry
        l=l.next
    if carry!=0:
        node=ListNode(carry)
        tail.next=node
        tail=node
    return head


if __name__=="__main__":
    l1=listToNode([9,9])
    l2=listToNode([9,9])
    printNode(addTwoNumbers(l1,l2))

