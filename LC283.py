class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        slow = fast = 0

        while fast < len_nums:
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]

                slow += 1

            fast += 1

        print(nums)

        # return nums

        # if len(nums) > 1:
        #     bound = len(nums) - 1
        #     curr = bound - 1

        #     while curr >= 0:
        #         if nums[curr] == 0:
        #             temp = curr

        #             while temp < bound:
        #                 nums[temp], nums[temp + 1] = nums[temp + 1], nums[temp]
        #                 temp += 1

        #             bound -= 1

        #         curr -= 1


sol = Solution()
# nums = [0,1,0,3,12]
# nums = [0, 0, 1]
# nums = [1,3,12,0,0]
# nums = [0, 1, 0, 3, 12]
nums = [0]
print(sol.moveZeroes(nums))
        