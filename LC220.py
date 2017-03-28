class Solution(object):
    def containsNearbyDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dup = {}
        for idx, num in enumerate(nums):
            for diff in range(t):
                temp = num + diff
                if temp in dup and idx - dup[temp] <= k:
                    return True                
            
            dup[num] = idx
        return False
