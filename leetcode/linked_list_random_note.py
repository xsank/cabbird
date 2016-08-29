import random
from structure.listnode import *


class Solution(object):
    def __init__(self,head):
        self.head=head

    def getRandom(self):
        count=0
        head=self.head
        while head:
            if random.randint(0,count)==count:
                res=head.val
            head=head.next
            count+=1
        return res


if __name__=="__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    solution = Solution(head)
    print solution.getRandom()
