# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        last = tail = head

        while n > 0:
            tail = tail.next
            n -= 1

        if not tail:
            return head.next

        while tail.next:
            last = last.next
            tail = tail.next

        last.next = last.next.next
        return head

n0 = ListNode(0)
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

# n0.next = n1
n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

sol = Solution()

new_head = sol.removeNthFromEnd(n1, 1)

while new_head:
    print(new_head.val)
    new_head = new_head.next
