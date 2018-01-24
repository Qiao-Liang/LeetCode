# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        heads = [None] * k

        if not root:
            return heads

        curr = root
        length = 0
        sec = 0

        while curr:
            length += 1
            curr = curr.next

        while k > 0 and root:
            count = length / k + (length % k > 0)
            length -= count
            heads[sec] = temp = root

            while count > 1:
                temp = temp.next
                count -= 1

            if temp:
                root = temp.next
                temp.next = None
            else:
                root = None
            
            sec += 1
            k -= 1

        return heads


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
# n5 = ListNode(5)
# n6 = ListNode(6)
# n7 = ListNode(7)
# n8 = ListNode(8)
# n9 = ListNode(9)

n1.next = n2
n2.next = n3
n3.next = n4
# n4.next = n5
# n5.next = n6
# n6.next = n7
# n7.next = n8
# n8.next = n9

sol = Solution()
res = sol.splitListToParts(n1, 5)

for link in res:
    print("*" * 30)
    while link:
        print(link.val)
        link = link.next
    
    print("*" * 30)
        