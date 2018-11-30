class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)


sol = Solution()
nums = [1,1,2,3,3,4,4,8,8]
print sol.singleNonDuplicate(nums)
