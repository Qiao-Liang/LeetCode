"""
Jump Game
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # length = len(nums)
        # temp = [False] * length
        # temp[0] = True
        
        # for i in range(1, length):
        #     for j in range(i):
        #         if temp[j] and nums[j] >= i - j:
        #             temp[i] = True
        #             break
        
        # return temp[-1]

        max_dist = 0

        for i in range(len(nums)):
            if i > max_dist:
                return False
            max_dist = max(max_dist, i + nums[i])
        
        return True
