from time import time

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = {()}

        for num in nums:
            result |= {s + (num,) for s in result if not s or s[-1] <= num}
        
        return [list(grp) for grp in result if len(grp) > 1]

        # subs = {()}
        # for num in nums:
        #     subs |= {sub + (num,)
        #             for sub in subs
        #             if not sub or sub[-1] <= num}
        # return [sub for sub in subs if len(sub) >= 2]

sol = Solution()
# nums = [4, 6, 7, 7]
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
t = time()
print(sol.findSubsequences(nums))
print(time() - t)