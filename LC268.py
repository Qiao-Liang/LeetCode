class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)

        return (len_nums + 1) * len_nums / 2 - sum(nums) 


sol = Solution()
nums = [9,6,4,2,3,5,7,0,1]
print(sol.missingNumber(nums))
