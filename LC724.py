class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        left_sum = 0
        right_sum = sum(nums[1:])
        len_nums = len(nums)
        pivot = 0

        while left_sum != right_sum:
            left_sum += nums[pivot]
            pivot += 1

            if pivot == len_nums:
                return -1
            
            right_sum -= nums[pivot]

        return pivot if left_sum == right_sum else -1


sol = Solution()
nums = [1, 7, 3, 6, 5, 6]
# nums = [1, 2, 3]
# nums = [-1,-1,-1,1,1,1]
# nums = [-1,-1,-1,-1,-1,0]
print(sol.pivotIndex(nums))
