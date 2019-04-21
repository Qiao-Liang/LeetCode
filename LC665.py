class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last = curr_max = -float('inf')
        desc_found = False

        for num in nums:
            if num < curr_max:
                if desc_found and num < last:
                    return False
                else:
                    desc_found = True
            
            last = num
            curr_max = max(num, curr_max)

        return True


sol = Solution()
# nums = [4,2,3]
# nums = [4,2,3,2]
nums = [3,4,2,3]
# nums = [4,2,1]
print(sol.checkPossibility(nums))
