# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next
        
        return prev


def test():
    nodes = []
    for i in range(1, 6):
        nodes.append(ListNode(i))

    for i in range(0, len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    head = nodes[0]

    sol = Solution()
    new_head = sol.reverseList(head)

    loop = new_head
    while loop:
        print(loop.val)
        loop = loop.next

    # for i in range(0, 5):
    #     if nodes[i].next:
    #         print(nodes[i].next.val)
    #     else:
    #         print('null')