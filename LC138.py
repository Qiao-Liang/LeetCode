# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        temp_head = last = RandomListNode(-1)
        curr = head
        
        while curr:
            temp = RandomListNode(curr.label)
            last.next = temp
            curr.ref = temp
            last = last.next
            curr = curr.next

        curr = head
        new_node = new_head = temp_head.next

        while curr:
            new_node.random = curr.random.ref if curr.random else None
            new_node = new_node.next
            curr = curr.next

        curr = head

        while curr:
            del curr.ref
            curr = curr.next

        return new_head

        
n1 = RandomListNode(1)
n2 = RandomListNode(2)
n3 = RandomListNode(3)
n4 = RandomListNode(4)
n5 = RandomListNode(5)
n6 = RandomListNode(6)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

n1.random = n4
n3.random = n1
n4.random = n6
n6.random = n2

sol = Solution()

new_head = sol.copyRandomList(n1)

while new_head:
    print('label: %d, random label: %d' % (new_head.label, new_head.random.label if new_head.random else -1))
    new_head = new_head.next
