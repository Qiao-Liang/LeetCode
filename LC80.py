class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0
        bound = len(nums)

        while curr < bound:
            while curr + 2 < bound and nums[curr + 2] == nums[curr]:
                nums.pop(curr + 2)
                bound -= 1
            
            curr += 1

        return bound


sol = Solution()
# nums = [1,1,1,2,2,3]
# nums = [0,0,1,1,1,1,2,3,3]
# nums = [1, 1, 1]
# nums = [0,0,0,0,3]
nums = [1, 2, 2, 2]
print sol.removeDuplicates(nums)
