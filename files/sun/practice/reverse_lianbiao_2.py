"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        def split_node(head,m):
            if m == 1:
                return (None, head)
            current_no = 2
            lh = head
            lt = head
            rh = head.next
            while current_no < m:
                lt = rh
                rh = rh.next
                current_no += 1
            lt.next = None
            return lh

        def reverse_listnode(head_a):
            current = None
            pre = None
            if head_a.next == None or head_a == None:
                return head_a
            while head_a.next != None:
                current = head_a
                head_a = current.next
                current.next = pre
                pre = current
            head_a.next = pre
            return head_a

        def connect_listnode(head,head_a):
            if head == None:
                return head_a
            if head_a == None:
                return head
            end = head
            while end.next != None:
                end = end.next
            end.next = head_a
            return head

        ll_l, ll_r,= split_node(head,n)
        ll_l, ll_c = split_node(ll_l_1,m)
        ll_c = reverse_listnode(ll_c)
        h = connect_listnode(ll_l, ll_c)
        h2 = connect_listnode(h,ll_r)
        return h2


def l2ll(l):
    h = None
    c = None
    for i in l:
        if h is None:
            h = ListNode(i)
            c = h
        else:
            c.next = ListNode(i)
            c = c.next
    return h

def ll2l(h):
    l = []
    c = h
    while(c):
        l.append(c)
        c = c.next
    return l


listaa = [3760, 2881, 7595, 3904, 5069, 4421, 8560, 8879, 8488, 5040, 5792, 56, 1007, 2270, 3403, 6062]
head = l2ll(listaa)
head = Solution().reverseBetween(head, 2, 7)
o = ll2l(head)
print(o)
