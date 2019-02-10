class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or k == 0:
            return False

        
        len_nums = len(nums)

        def check_window(window):
            window.sort()

            for idx in range(1, len(window)):
                if window[idx] - window[idx - 1] <= t:
                    return True
            
            return False

        if k >= len_nums:
            return check_window(nums)

        srt = 0
        len_window = k + 1

        while srt + k < len_nums:
            if check_window(nums[srt: srt + len_window]):
                return True

            srt += 1

        return False


sol = Solution()
nums = [1, 5, 9, 1, 5, 9]
k = 1
t = 2

# nums = [1,2,3,1]
# k = 3
# t = 0

# nums = [1,0,1,1]
# k = 1
# t = 2

# nums = [0]
# k = 0
# t = 0

# nums = [2, 2]
# k = 3
# t = 0

print(sol.containsNearbyAlmostDuplicate(nums, k, t))
