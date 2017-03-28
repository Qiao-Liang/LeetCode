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
        pointer = head
        
        while pointer:
            temp = pointer.next
            while temp and pointer.val == temp.val:
                temp = temp.next
            
            pointer.next = temp
            pointer = temp
        
        return head