class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        up = down = 1

        for idx, num in enumerate(nums[1:], start=1):
            if num > nums[idx - 1]:
                up = down + 1
            elif num < nums[idx - 1]:
                down = up + 1
        
        return max(up, down)

        # len_nums = len(nums)
        # up = [1] * len_nums
        # down = [1] * len_nums

        # for idx, num in enumerate(nums[1:], start=1):
        #     if num > nums[idx - 1]:
        #         up[idx] = down[idx - 1] + 1
        #         down[idx] = down[idx - 1]
        #     elif num < nums[idx - 1]:
        #         down[idx] = up[idx - 1] + 1
        #         up[idx] = down[idx - 1]
        #     else:
        #         down[idx] = down[idx - 1]
        #         up[idx] = up[idx - 1]
        
        # return max(down[-1], up[-1])

        # len_nums = len(nums)

        # if len_nums < 2:
        #     return len_nums

        # memo = [None] * len_nums

        # for idx in range(1, len_nums):
        #     diff = nums[idx] - nums[idx - 1]
        #     memo[idx] = (1 if diff == 0 else 2, diff)

        # for curr_idx in range(2, len_nums):
        #     max_len = memo[curr_idx][0]

        #     for last_idx in range(1, curr_idx):
        #         diff = nums[curr_idx] - nums[last_idx]

        #         if diff * memo[last_idx][1] < 0:
        #             max_len = max(max_len, memo[last_idx][0] + 1)
                
        #     memo[curr_idx] = (max_len, diff)
        
        # return memo[-1][0]


sol = Solution()
# nums = [1,7,4,9,2,5]
nums = [1,17,5,10,13,15,10,5,16,8]
# nums = [84]
# nums = [1,2,3,4,5,6,7,8,9]
# nums = [0, 0, 0, 0]
print(sol.wiggleMaxLength(nums))
