class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        queue = []

        for num in nums:
            if num not in queue:
                queue.append(num)
                queue.sort()

            if len(queue) > 3:
                queue.pop(0)
        
        return queue[0] if len(queue) == 3 else queue[-1]


sol = Solution()
print sol.thirdMax([1, 2])
