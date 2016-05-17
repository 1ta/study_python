"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

"""
class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """

    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = ListNode(0)
        l3 = head
        while l1 and l2:
            if l1.val < l2.val:
                l3 = l1
                l1 = l1.next
                l3 = l3.next
            else:
                l3 = l2
                l2 = l2.next
                l3 =l3.next
        if l1:
            l3.next = l1
        if l2:
            l3.next = l2
        return head
