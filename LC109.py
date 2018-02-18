# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        slow, fast = head, head.next.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        temp = slow.next
        slow.next = None

        temp_head = TreeNode(temp.val)
        temp_head.left = self.sortedListToBST(head)
        temp_head.right = self.sortedListToBST(temp.next)

        return temp_head

        # if not head:
        #     return None

        # temp_list = []
        # curr = head

        # while curr:
        #     temp_list.append(curr.val)
        #     curr = curr.next

        # def recurse(srt, end):
        #     if end - srt < 1:
        #         return None
            
        #     mid = (end + srt) / 2
        #     temp_head = TreeNode(temp_list[mid])
        #     temp_head.left = recurse(srt, mid)
        #     temp_head.right = recurse(mid + 1, end)

        #     return temp_head

        # return recurse(0, len(temp_list))


sol = Solution()

n1 = ListNode(-10)
n2 = ListNode(-3)
n3 = ListNode(0)
n4 = ListNode(5)
n5 = ListNode(9)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

from time import time
srt = time()

new_head = sol.sortedListToBST(n1)

print("Time elapsed: {}".format(time() - srt))

queue = [new_head]

while queue:
    temp = queue.pop(0)
    print(temp.val)

    if temp.left:
        queue.append(temp.left)
    
    if temp.right:
        queue.append(temp.right)
        