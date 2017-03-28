# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head:
            pointer = head
            rev_head = ListNode(pointer.val)
            
            while pointer and pointer.next:
                temp = ListNode(pointer.next.val)
                temp.next = rev_head
                rev_head = temp
                pointer = pointer.next
            
            while head and rev_head and head.next and rev_head.next:
                if head.val == rev_head.val:
                    head = head.next
                    rev_head = rev_head.next
                else:
                    return False
            
            return True
        else:
            return True