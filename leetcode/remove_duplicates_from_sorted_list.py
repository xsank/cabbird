from structure.listnode import *

def deleteDuplicates(head):
    flag=1<<32
    q=p=head
    while p:
        if p.val!=flag:
            flag=p.val
            q=p
        else:
            q.next=p.next
        p=p.next
    return head


if __name__=="__main__":
    _list=listToNode([1,1,2,3,3,3])
    printNode(deleteDuplicates(_list))
