from structure.listnode import *

def rotateRight(head,k):
    if head:
        _len=1
        p=head
        while p.next:
            p=p.next
            _len+=1
        p.next=head
        k%=_len
        move=_len-k
        while move:
            p=p.next
            move-=1
        head=p.next
        p.next=None
    return head



if __name__=="__main__":
    head=listToNode([1,2,3,4,5])
    head=rotateRight(head,2)
    printNode(head)
