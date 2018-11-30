class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        minstack = []
        maxstack = [nums[-1]]

        for num in reversed(nums[:len(nums) - 1]):
            if minstack and minstack[-1] > num:
                return True

            while maxstack and maxstack[-1] < num:
                minstack.append(maxstack.pop())

            maxstack.append(num)

        return False

        # bound = len(nums) - 1
        # idx = 0

        # while idx < bound:
        #     if nums[idx] > nums[idx + 1]:
        #         nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
        #         idx += 1
        #     else:
        #         break
        
        # return idx < bound - 1 and min(nums[:idx + 1]) < max(nums[idx + 2:]) < nums[idx + 1]


sol = Solution()
# nums = [-1, 3, 2, 0]
# nums = [1, 2, 3, 4]
# nums = [3, 1, 4, 2]
# nums = [2, 1, 3]
nums = [3, 5, 0, 3, 4]
print sol.find132pattern(nums)
        