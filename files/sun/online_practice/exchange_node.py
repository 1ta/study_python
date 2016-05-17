# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        temp1 = ListNode(0)
        temp1.next = head
        head = temp1
        p1 = temp1
        p2 = p1.next
        p3 = p2.next
        while p1.next:
            if p3 is None:
                return head
            else:
                p4 = p3.next
                p1.next = p3
                p3.next = p2
                p2.next = p4
                p1 = p1.next.next
        return head.next
