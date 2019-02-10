class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        return [key for key, val in counts.items() if val == 1]


sol = Solution()
nums = [1,2,1,3,2,5]
print(sol.singleNumber(nums))
