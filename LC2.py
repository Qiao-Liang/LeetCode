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
        carry = 0
        head = ListNode(None)
        last = head

        while l1 or l2 or carry > 0:
            temp = carry

            if l1:
                temp += l1.val
                l1 = l1.next

            if l2:
                temp += l2.val
                l2 = l2.next

            if temp > 9:
                temp = temp % 10
                carry = 1
            else:
                carry = 0

            tail = ListNode(temp)
            last.next = tail
            last = tail

        return head.next


    def addTwoNumbers_Draft(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = ListNode(None)
        last = head

        while l1 and l2:
            temp, carry = self.get_digit_carry(l1.val + l2.val, carry)

            tail = ListNode(temp)
            last.next = tail
            last = tail
            l1 = l1.next
            l2 = l2.next

        while l1:
            temp, carry = self.get_digit_carry(l1.val, carry)

            tail = ListNode(temp)
            last.next = tail
            last = tail
            l1 = l1.next

        while l2:
            temp, carry = self.get_digit_carry(l2.val, carry)

            tail = ListNode(temp)
            last.next = tail
            last = tail
            l2 = l2.next

        if carry > 0:
            last.next = ListNode(carry)

        return head.next

    def get_digit_carry(self, digit, carry):
        temp = digit + carry

        if temp > 9:
            return temp % 10, 1
        else:
            return temp, 0

l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l2 = ListNode(1)

sol = Solution()
result = sol.addTwoNumbers(l1, l2)

while result:
    print(result.val)
    result = result.next