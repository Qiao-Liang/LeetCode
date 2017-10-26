# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 2:
            return head

        temp = ListNode(-1)
        temp.next = head
        last = None
        curr = head
        next = None
        count = k
        sec_head = None
        sec_tail = None
        hook = temp

        while curr:
            if count == k:
                sec_head = sec_tail = curr
                num = k
                while sec_head and num > 0:
                    num -= 1
                    if num > 0:
                        sec_head = sec_head.next
                
                if num > 0:
                    hook.next = sec_tail
                    break
                else:
                    hook.next = sec_head

            next = curr.next
            curr.next = last
            last = curr
            curr = next
            count -= 1

            if count == 0:
                count = k
                hook = sec_tail
                sec_tail.next = None

        return temp.next


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

new_head = sol.reverseKGroup(n1, 3)

# print (new_head.val)

while new_head:
    print(new_head.val)
    new_head = new_head.next
