class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        last_idx = len(nums) - 1
        not_found = True
        dest = 0

        for idx in range(last_idx, 0, -1):
            if nums[idx] > nums[idx - 1]:
                dest = idx - 1
                not_found = False
                break
            
        if not_found:
            nums.reverse()
        else:
            for chk in range(last_idx, dest, -1):
                if nums[chk] > nums[dest]:
                    nums[dest], nums[chk] = nums[chk], nums[dest]
                    break

            nums[idx:] = sorted(nums[idx:])


sol = Solution()
# nums = [4,2,0,2,3,2,0]
nums = [1, 3, 2]
sol.nextPermutation(nums)
print(nums)
