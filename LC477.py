class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        res = 0
        max_num = max(nums)
        temp = 1

        while temp <= max_num:
            zeros = ones = 0
            
            for num in nums:
                if num & temp:
                    ones += 1
                else:
                    zeros += 1

            res += ones * zeros
            temp <<= 1

        return res


sol = Solution()
# nums = [4, 14, 2]
nums = [6,1,8,6,8]
print sol.totalHammingDistance(nums)
