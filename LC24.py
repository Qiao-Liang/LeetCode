# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp_node = ListNode(-1)
        temp_node.next = head
        curr = temp_node

        while curr.next and curr.next.next:
            node1 = curr.next
            node2 = node1.next

            node1.next = node2.next
            node2.next = node1
            curr.next = node2

            curr = curr.next.next

        return temp_node.next


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
new_head = sol.swapPairs(n1)

while new_head:
    print(new_head.val)
    new_head = new_head.next
