class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
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

        dup = {}
        for idx, num in enumerate(nums):
            if num in dup and idx - dup[num] <= k:
                return True
            else:
                dup[num] = idx
        
        return False
