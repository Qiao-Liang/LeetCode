# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head and head.next:
            fast = slow = curr = head

            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next

            sec_half = slow.next
            slow.next = None
            rev_head = None

            while sec_half:
                temp_next = sec_half.next
                sec_half.next = rev_head
                rev_head = sec_half
                sec_half = temp_next

            while rev_head:
                next_curr = curr.next
                next_rev_head = rev_head.next
                
                curr.next = rev_head
                rev_head.next = next_curr

                curr = next_curr
                rev_head = next_rev_head
                
        return head


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

sol = Solution()
new_head = sol.reorderList(n1)

while new_head:
    print(new_head.val)
    new_head = new_head.next
