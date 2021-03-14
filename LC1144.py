class Solution:
    def movesToMakeZigzag(self, nums) -> int:
        res0 = res1 = 0
        nums1 = nums[:]
        
        for i in range(1, len(nums)):
            if i & 1:
                if nums[i] <= nums[i - 1]:
                    res0 += nums[i - 1] - nums[i] + 1
                    nums[i - 1] = nums[i] - 1
                
                if nums1[i] >= nums1[i - 1]:
                    res1 += nums1[i] - nums1[i - 1] + 1
                    nums1[i] = nums1[i - 1] - 1
            else:
                if nums[i] >= nums[i - 1]:
                    res0 += nums[i] - nums[i - 1] + 1
                    nums[i] = nums[i - 1] - 1

                if nums1[i] <= nums1[i - 1]:
                    res1 += nums1[i - 1] - nums1[i] + 1
                    nums1[i - 1] = nums1[i] - 1
        
        return min(res0, res1)


sol = Solution()
# p = [9,6,1,6,2]
# p = [2,7,10,9,8,9]
# p = [2,1,2]
p = [3,1,7,4,4,1,1,10,10,9]
print(sol.movesToMakeZigzag(p))
