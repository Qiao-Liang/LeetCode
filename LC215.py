class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return None

        end = len(nums)

        if end < 2:
            return nums[0]

        srt = 0
        target = end - k

        while True:
            pivot = nums[srt]
            wall = srt

            for idx in xrange(srt + 1, end):
                if nums[idx] < pivot:
                    wall += 1
                    if idx != wall:
                        nums[idx], nums[wall] = nums[wall], nums[idx]

            nums[srt], nums[wall] = nums[wall], nums[srt]

            if wall < target:
                srt = wall + 1
            elif wall > target:
                end = wall
            else:
                return nums[wall]


sol = Solution()
# nums = [3, 2, 1, 5, 6, 4]
# nums = [99, 99]

import random
from time import time
nums = random.sample(range(0, 100000), 100000)

t = time()
print sol.findKthLargest(nums, 50000)
print time() - t
