# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        curr = head.next
        sort = head
        sort.next = None

        while curr:
            temp = sort
            hook = None
            temp_next = curr.next

            while temp:
                if temp.val > curr.val:
                    break
                else:
                    hook = temp
                    temp = temp.next

            if hook:
                temp_hook_next = hook.next
                hook.next = curr
                curr.next = temp_hook_next
            else:
                curr.next = sort
                sort = curr

            curr = temp_next

        return sort


# n1 = ListNode(3)
# n2 = ListNode(2)
# n3 = ListNode(4)
# n4 = ListNode(1)
# n5 = ListNode(1)
# n6 = ListNode(5)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6

n1 = ListNode(2)
n2 = ListNode(1)

n1.next = n2

sol = Solution()
new_head = sol.insertionSortList(n1)

while new_head:
    print(new_head.val)
    new_head = new_head.next
