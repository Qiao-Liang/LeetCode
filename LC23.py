# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        length = len(lists)

        if not lists or length == 0:
            return None
        if length < 2:
            return lists[0]

        head = ListNode(-1)
        last = head
        lists = [node for node in lists if node]

        def sift(heap, parent):
            '''
            Sift down larger values
            '''
            last_child = parent * 2 + 1
            length = len(heap)

            while last_child < length:
                if last_child + 1 < length and heap[last_child + 1].val < heap[last_child].val:
                    last_child += 1

                if heap[parent].val > heap[last_child].val:
                    heap[parent], heap[last_child] = heap[last_child], heap[parent]
                
                parent = last_child
                last_child = last_child * 2 + 1

        last_parent = (length - 1) / 2
        for idx in range(last_parent, -1, -1):
            sift(lists, idx)

        while lists:
            last.next = lists[0]
            last = lists[0]
            
            if last.next:
                lists[0] = last.next
            else:
                lists[0] = lists[-1]
                lists.pop()

            sift(lists, 0)

        return head.next

# n0 = ListNode(0)
# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(4)
# n5 = ListNode(5)
# n6 = ListNode(6)
# n7 = ListNode(7)
# n8 = ListNode(8)
# n9 = ListNode(9)
# n10 = ListNode(10)
# n11 = ListNode(11)
# n12 = ListNode(12)
# n13 = ListNode(13)
# n14 = ListNode(2)

# n1.next = n3
# n3.next = n6
# n6.next = n9

# n14.next = n2
# n2.next = n4
# n4.next = n7
# n7.next = n10

# n5.next = n8
# n8.next = n11

# n12.next = n13

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(2)
n4 = ListNode(1)
n5 = ListNode(1)
n6 = ListNode(2)

n1.next = n2
n2.next = n3

n4.next = n5
n5.next = n6

sol = Solution()
# head = sol.mergeKLists([n1, n2, n5, n12])
head = sol.mergeKLists([n1, n4])

while head:
    print(head.val)
    head = head.next
