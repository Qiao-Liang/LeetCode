class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False

        window = nums[:k + 1]
        bound = len(nums)
        left = 0
        right = k + 1

        while True:
            window.sort()

            for idx in range(k):
                if abs(window[idx] - window[idx + 1]) <= t:
                    return True

            window.remove(nums[left])
            left += 1
            right += 1

            if right < bound:
                window.append(nums[right])
            else:
                break
        
        return False


        # dup = {}
        # for idx, num in enumerate(nums):
        #     for diff in range(t):
        #         temp = num + diff
        #         if temp in dup and idx - dup[temp] <= k:
        #             return True                
            
        #     dup[num] = idx
        # return False


sol = Solution()
nums = [1, 5, 9, 1, 5, 9]
k = 1
t = 2

for idx in range(100):
    print('*' * 60)

sol.containsNearbyAlmostDuplicate(nums, k, t)
