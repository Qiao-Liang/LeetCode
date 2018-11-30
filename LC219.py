class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dup = {}
        for idx, num in enumerate(nums):
            if num in dup and idx - dup[num] <= k:
                return True
            else:
                dup[num] = idx
        
        return False

        '''
        Version 1
        '''
        # length = len(nums)
        
        # for i in range(length):
        #     temp = 1
        #     while temp <= k:
        #         if i + temp < length and nums[i] == nums[i + temp]:
        #             return True
                
        #         temp += 1
        
        # return False


        # temp = []
        # keys = {}
        # for num in nums:
        #     temp.append(num)

        #     if num in keys:
        #         return True
        #     else:
        #         keys[num] = ''

        #     if len(temp) > k:
        #         d = temp.pop(0)
        #         del keys[d]

        # return False


sol = Solution()
# nums = [1,2,3,1,2,3]
# k = 2
nums = [1,0,1,1]
k = 1
print(sol.containsNearbyDuplicate(nums, k))
