class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        c = head
        p = None
        while c:
            if val == c.val:
                head = c.next
            p = c
            c = c.next


inputList = [5]
head = None
tail = None
for value in inputList:
    node = ListNode(value)
    if head is None:
        head = node
        tail = node
    else:
        tail.next = node
        tail = node


Solution().removeElements(head, 1)

c = head
while c:
    print(c.val)
    c = c.next
