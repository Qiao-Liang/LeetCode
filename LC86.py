# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        smaller = curr_sm = ListNode(-1)
        greater = curr_gt = ListNode(-1)
        curr = head

        while curr:
            if curr.val < x:
                curr_sm.next = curr
                curr_sm = curr_sm.next
            else:
                curr_gt.next = curr
                curr_gt = curr_gt.next

            curr = curr.next

        curr_sm.next = greater.next
        curr_gt.next = None

        return smaller.next

    def partition2(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        temp_head = ListNode(-1)
        temp_head.next = head
        hook = temp_head

        while hook:
            if hook.next and hook.next.val < x:
                hook = hook.next
            else:
                break
        
        curr = last = hook.next
        
        while curr:
            if curr.val < x:
                temp_next = curr.next
                temp_hook_next = hook.next
                hook.next = curr
                curr.next = temp_hook_next
                last.next = temp_next
                hook = curr
                curr = temp_next
            else:
                last = curr
                curr = curr.next

        return temp_head.next


# n1 = ListNode(1)
# n2 = ListNode(4)
# n3 = ListNode(3)
# n4 = ListNode(2)
# n5 = ListNode(5)
# n6 = ListNode(2)

n1 = ListNode(3)
n2 = ListNode(1)
n3 = ListNode(2)

n1.next = n2
n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6

sol = Solution()
new_head = sol.partition(n1, 3)

while new_head:
    print(new_head.val)
    new_head = new_head.next
