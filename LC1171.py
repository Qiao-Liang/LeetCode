from collections import OrderedDict

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeZeroSumSublists(self, head):
        curr = dummy = ListNode(0)
        dummy.next = head
        pre_sum = 0
        visited = OrderedDict()

        while curr:
            pre_sum += curr.val
            node = visited.get(pre_sum, curr)

            while pre_sum in visited:
                visited.popitem()

            visited[pre_sum] = node
            node.next = curr = curr.next
        
        return dummy.next


        # accu_sum = [head.val]
        # temp = head.next
        # dict = {head.val: 0}
        # i = 1
        # to_del = set([])
        # is_new = True
        # total = head.val

        # if head.val == 0:
        #     to_del.add(0)
        
        # while temp:
        #     if temp.val == 0:
        #         to_del.add(i)

        #     total += temp.val
        #     temp_sum = accu_sum[-1] + temp.val
        #     accu_sum.append(temp_sum)

        #     if temp_sum in dict:
        #         for ti in range(dict[temp_sum] + 1, i + 1):
        #             to_del.add(ti)

        #             if accu_sum[ti] in dict:
        #                 del dict[accu_sum[ti]]
        #         is_new = False
        #     elif temp_sum == 0 and is_new:
        #         to_del.update([ti for ti in range(i + 1)])
        #         is_new = False
            
        #     dict[temp_sum] = i
        #     i += 1
        #     temp = temp.next
        
        # if total == 0:
        #     return None

        # temp_head = ListNode(None)
        # last = temp_head
        # temp = head
        # i = 0
        
        # while temp:
        #     if i not in to_del:
        #         last.next = temp
        #         last = temp
        #     else:
        #         last.next = None
                
        #     temp = temp.next
        #     i += 1
        
        # return temp_head.next


def create_list(arr):
    head = ListNode(arr[0])
    last = head

    for n in arr[1:]:
        temp = ListNode(n)
        last.next = temp
        last = temp

    return head


sol = Solution()
# arr = [1,2,-3,3,1]
# arr = [1,2,3,-3,-2]
# arr = [1,-1]
# arr = [1,2,3,-3,3]
# arr = [0]
# arr = [0, 2]
# arr = [2, 1, -3]
arr = [1,0,0,-1,2,-1,0]
head = create_list(arr)
res = sol.removeZeroSumSublists(head)

while res:
    print(res.val)
    res = res.next
