class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        c = 0
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if c == 1:
                    return False
                
                c += 1
                
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                
        return True


sol = Solution()
# nums = [4,2,3]
# nums = [4,2,3,2]
nums = [3,4,2,3]
# nums = [4,2,1]
print(sol.checkPossibility(nums))
