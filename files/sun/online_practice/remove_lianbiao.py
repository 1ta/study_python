"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        def findend(head):
            end = head
            count = 1
            while end.next != None:
                end = end.next
                count = count+1
            return count

        def removenode(head,m):
            if head.next is None:
                return None
            if m == 1 :
                return head.next
            current_no = 2
            lh = head
            lt = head
            rh = head.next
            while current_no < m:
                lt = rh
                rh = rh.next
                current_no += 1
            lt.next = rh.next
            return head


        l = findend(head)
        m = l+1-n
        r = removenode(head,m)
        return r
