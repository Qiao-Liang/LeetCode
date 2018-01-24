# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None

        temp_head = last = ListNode(-1)
        temp_head.next = head
        curr = head
        
        while curr:
            if curr.val == val:
                last.next = curr.next
                curr.next = None
                curr = last.next
            else:
                last = curr
                curr = curr.next

        return temp_head.next


sol = Solution()

# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(6)
# n4 = ListNode(3)
# n5 = ListNode(4)
# n6 = ListNode(5)
# n7 = ListNode(6)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6
# n6.next = n7

n1 = ListNode(1)
n2 = ListNode(1)

n1.next = n2

new_head = sol.removeElements(n1, 1)

while new_head:
    print(new_head.val)
    new_head = new_head.next
        