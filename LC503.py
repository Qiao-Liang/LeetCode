class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_nums = len(nums)
        res = [0] * len_nums
        stack = []

        for idx in range((len_nums << 1) - 1, -1, -1):
            temp_idx = idx % len_nums

            while stack and nums[stack[-1]] <= nums[temp_idx]:
                stack.pop()

            res[temp_idx] = nums[stack[-1]] if stack else -1
            stack.append(temp_idx)

        return res


        # res = []
        # len_nums = len(nums)

        # for idx, num in enumerate(nums):
        #     temp_idx = (idx + 1) % len_nums

        #     while temp_idx != idx and nums[temp_idx] <= num:
        #         temp_idx += 1
        #         temp_idx %= len_nums

        #     if temp_idx == idx:
        #         res.append(-1)
        #     else:
        #         res.append(nums[temp_idx])

        # return res


sol = Solution()
# nums = [1,2,1]
nums = [3, 8, 4, 1, 2]
print(sol.nextGreaterElements(nums))
