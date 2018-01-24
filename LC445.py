# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or (l1.val == 0 and not l1.next):
            return l2

        if not l2 or (l2.val == 0 and not l2.next):
            return l1
        
        def reverse(head):
            last = None
            curr = head

            while curr:
                temp_next = curr.next
                curr.next = last
                last = curr
                curr = temp_next

            return last

        rev_l1 = reverse(l1)
        rev_l2 = reverse(l2)
        carry = 0
        temp_head = curr = ListNode(-1)

        while rev_l1 and rev_l2:
            temp_sum = rev_l1.val + rev_l2.val + carry

            if temp_sum > 9:
                temp_sum %= 10
                carry = 1
            else:
                carry = 0

            curr.next = ListNode(temp_sum)
            curr = curr.next
            rev_l1 = rev_l1.next
            rev_l2 = rev_l2.next

        remain = rev_l1 if rev_l1 else rev_l2

        while remain:
            if carry == 0:
                curr.next = ListNode(remain.val)
            else:
                temp_sum = remain.val + carry
                if temp_sum > 9:
                    temp_sum %= 10
                    carry = 1
                else:
                    carry = 0
                
                curr.next = ListNode(temp_sum)
            
            curr = curr.next
            remain = remain.next
        
        if carry == 1:
            curr.next = ListNode(1)
            curr = curr.next
        
        return reverse(temp_head.next)


sol = Solution()

# n11 = ListNode(7)
# n12 = ListNode(2)
# n13 = ListNode(4)
# n14 = ListNode(3)

# n11.next = n12
# n12.next = n13
# n13.next = n14

# n21 = ListNode(5)
# n22 = ListNode(6)
# n23 = ListNode(4)

# n21.next = n22
# n22.next = n23

n11 = ListNode(9)
n12 = ListNode(9)
n13 = ListNode(9)
n14 = ListNode(9)

n11.next = n12
n12.next = n13
n13.next = n14

n21 = ListNode(5)

new_head = sol.addTwoNumbers(n11, n21)

while new_head:
    print(new_head.val)
    new_head = new_head.next
