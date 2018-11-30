class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = twos = 0

        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        count = 0
        temp = 1
        res = 0

        for idx in xrange(32):
            ones = 0

            for num in nums:
                if num & temp:
                    ones += 1

            if ones % 3 == 1:
                res |= temp

            temp <<= 1

        if res > 1 << 31:
            return res - (1 << 32)
        else:
            return res
    

sol = Solution()
# nums = [1, 2, 1, 2, 3, 1, 4, 2, 4, 4]
nums = [1, 2, 1, 1]
# nums = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
# nums = [-401451,-177656,-2147483646,-473874,-814645,-2147483646,-852036,-457533,-401451,-473874,-401451,-216555,-917279,-457533,-852036,-457533,-177656,-2147483646,-177656,-917279,-473874,-852036,-917279,-216555,-814645,2147483645,-2147483648,2147483645,-814645,2147483645,-216555]
print sol.singleNumber(nums)
