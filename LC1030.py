# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        res, stack = [], []

        while head:
            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val

            stack.append([len(res), head.val])
            res.append(0)
            head = head.next

        return res


sol = Solution()
# temp = [2,1,5]
# temp = [2,7,4,3,5]
temp = [1,7,5,1,9,2,5,1]
print(sol.nextLargerNodes(temp))
