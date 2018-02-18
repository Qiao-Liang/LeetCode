# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        curr = head
        list_len = 0

        while curr and curr.next:
            if curr.next.val < curr.val:
                curr.val, curr.next.val = curr.next.val, curr.val
            
            curr = curr.next.next
            list_len += 2

        if curr:
            list_len += 1

        merge_len = 2
        temp_head = ListNode(-1)
        temp_head.next = head

        while list_len > merge_len:
            curr = temp_head.next
            hook = temp_head

            while curr:
                temp1 = temp2 = curr
                temp_curr = hook
                counter = 0

                while counter < merge_len and temp2:
                    temp2 = temp2.next
                    counter += 1

                next_curr = temp2
                counter = 0

                while counter < merge_len and next_curr:
                    next_curr = next_curr.next
                    counter += 1

                counter1 = counter2 = 0

                while counter1 < merge_len and counter2 < merge_len and temp1 and temp2:
                    if temp1.val < temp2.val:
                        temp_curr.next = temp1
                        temp1 = temp1.next
                        counter1 += 1
                    else:
                        temp_curr.next = temp2
                        temp2 = temp2.next
                        counter2 += 1
                    
                    temp_curr = temp_curr.next

                while counter1 < merge_len and temp1:
                    temp_curr.next = temp1
                    temp1 = temp1.next
                    counter1 += 1
                    temp_curr = temp_curr.next

                while counter2 < merge_len and temp2:
                    temp_curr.next = temp2
                    temp2 = temp2.next
                    counter2 += 1
                    temp_curr = temp_curr.next

                hook = temp_curr
                hook.next = None
                curr = next_curr
            
            merge_len *= 2

        return temp_head.next


sol = Solution()

n0 = ListNode(3)
n1 = ListNode(2)
n2 = ListNode(6)
n3 = ListNode(5)
n4 = ListNode(1)
n5 = ListNode(4)
n6 = ListNode(7)
n7 = ListNode(9)
n8 = ListNode(8)
n9 = ListNode(0)
n10 = ListNode(10)

n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n10

new_head = sol.sortList(n0)

while new_head:
    print(new_head.val)
    new_head = new_head.next
