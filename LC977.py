class Solution:
    # def sortedSquares(self, A):
    #     """
    #     :type A: List[int]
    #     :rtype: List[int]
    #     """
    #     return sorted(map(lambda x: x * x, A))

    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0:
            return [n ** 2 for n in nums]
        elif nums[-1] <= 0:
            return [n ** 2 for n in reversed(nums)]
        
        len_nums = len(nums)
        l, r = 0, len_nums
        m = 0
        
        while l < r:
            m = (l + r) // 2
            
            if nums[m] < 0 and nums[m + 1] >= 0:
                break
            elif nums[m] < 0:
                l = m + 1
            elif 0 <= nums[m]:
                r = m
        
        l = m
        r = m + 1
        res = []
        
        while l > -1 and r < len_nums:
            if abs(nums[l]) < abs(nums[r]):
                res.append(nums[l] ** 2)
                l -= 1
            else:
                res.append(nums[r] ** 2)
                r += 1
                
        while l > -1:
            res.append(nums[l] ** 2)
            l -= 1
        
        while r < len_nums:
            res.append(nums[r] ** 2)
            r += 1
        
        return res
        


sol = Solution()
# a = [-4,-1,0,3,10]
a = []
print(sol.sortedSquares(a))
