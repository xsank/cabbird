def getIntersectionNode(headA, headB):
    pa=headA
    pb=headB
    while pa or pb:
        pa=pa.next
        pb=pb.next
