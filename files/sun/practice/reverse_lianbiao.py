"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list.
                  Reverse it in-place.
    """
    def reverse(self, head):
        current = None
        pre = None
        if head.next == None or head == None:
            return head
        while head.next != None:
            current = head
            head = current.next
            current.next = pre
            pre = current
        head.next = pre
        return head
