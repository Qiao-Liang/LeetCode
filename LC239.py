# from collections import defaultdict
# from heapq import heapify, heappop, heappush

# class Solution:
#     def maxSlidingWindow(self, nums, k: int):
#         if not nums or not k:
#             return []

#         count = defaultdict(int)
#         heap = [-n for n in nums[:k]]
#         heapify(heap)
#         res = [-heap[0]]

#         for i in range(k, len(nums)):
#             heappush(heap, -nums[i])
#             count[-nums[i - k]] += 1

#             while count[heap[0]] > 0:
#                 count[heap[0]] -= 1
#                 heappop(heap)

#             res.append(-heap[0])

#         return res

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        q = deque()
        res = []
        
        for i, n in enumerate(nums):
            while q and n >= nums[q[-1]]:
                q.pop()
                
            q.append(i)
            
            if i - k + 1 >= 0:
                res.append(nums[q[0]])
                
            if i - k + 1 >= q[0]:
                q.popleft()
            
        return res


sol = Solution()
p = [[1,3,-1,-3,5,3,6,7], 3]
print(sol.maxSlidingWindow(*p))
