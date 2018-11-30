# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        last = temp_head = ListNode(None)
        temp_head.next = curr = head

        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next

            if last.next == curr:
                last = curr
                curr = curr.next
            else:
                curr = curr.next
                last.next = curr

        return temp_head.next


sol = Solution()

n0 = ListNode(1)
n1 = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(2)
n4 = ListNode(3)
n5 = ListNode(4)
n6 = ListNode(5)

n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

new_head = sol.deleteDuplicates(n0)
while new_head:
    print new_head.val
    new_head = new_head.next
        