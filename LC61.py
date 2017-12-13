# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        if not head.next or k == 0:
            return head

        hook = head
        new_head = head
        last = None
        dist = k
        counter = 0

        while dist > 1 and hook:
            hook = hook.next
            dist -= 1
            counter += 1

        if hook and not hook.next and dist == 1:
            return head
        
        if not hook:
            return self.rotateRight(head, k % counter)

        while hook.next:
            hook = hook.next
            last = new_head
            new_head = new_head.next

        if last:
            last.next = None
        hook.next = head

        return new_head

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
new_head = sol.rotateRight(n1, 7)

while new_head:
    print(new_head.val)
    new_head = new_head.next
