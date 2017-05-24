class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        temp = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[temp] = nums[i]
                temp += 1
                
        return temp