# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        index = 1
        curr = head
        prev = None
        next = None
        
        while index < m:
            prev = curr
            curr = curr.next
            index += 1
        
        section_hook = prev
        section_tail = curr
        
        while m <= index and index <= n:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

            index += 1
            
        section_tail.next = next

        if section_hook:
            section_hook.next = prev

            return head
        else:
            return prev

def test(m, n):
    nodes = []
    for i in range(1, 6):
        nodes.append(ListNode(i))

    for i in range(0, len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    head = nodes[0]

    sol = Solution()
    new_head = sol.reverseBetween(head, m, n)

    print(new_head.val)
    
    print("*" * 90)

    loop = new_head
    while loop:
        print(loop.val)
        loop = loop.next

