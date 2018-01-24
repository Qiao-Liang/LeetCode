# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        curr = head
        odd_head = odd_curr = ListNode(-1)
        even_head = even_curr = ListNode(-1)
        index = 1

        while curr:
            if index & 1 == 1:
                odd_curr.next = curr
                odd_curr = odd_curr.next
            else:
                even_curr.next = curr
                even_curr = even_curr.next

            curr = curr.next
            index += 1

        even_curr.next = None
        odd_curr.next = even_head.next

        return odd_head.next


sol = Solution()

n1 = ListNode(2)
n2 = ListNode(1)
n3 = ListNode(4)
n4 = ListNode(3)
n5 = ListNode(6)
n6 = ListNode(5)
n7 = ListNode(7)
n8 = ListNode(8)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8

new_head = sol.oddEvenList(n1)
while new_head:
    print(new_head.val)
    new_head = new_head.next
        