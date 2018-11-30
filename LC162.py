class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        
        return left


        # len_nums = len(nums)

        # if len_nums == 0:
        #     return None
        # elif len_nums == 1:
        #     return 0
        # else:
        #     left = 0
        #     right = bound = len_nums - 1

        #     while left <= right:
        #         mid = (left + right) // 2

        #         if (mid == 0 and nums[mid] > nums[mid + 1]) or (mid == bound and nums[mid] > nums[mid - 1]) or (nums[mid - 1] < nums[mid] > nums[mid + 1]):
        #             return mid
        #         elif (mid == 0 and nums[mid] < nums[mid + 1]) or (nums[mid - 1] < nums[mid] < nums[mid + 1]):
        #             left = mid + 1
        #         elif (mid == bound and nums[mid] < nums[mid - 1]) or (nums[mid - 1] > nums[mid] > nums[mid +1]):
        #             right = mid - 1

        # len_nums = len(nums)

        # if len_nums == 0:
        #     return None
        # elif len_nums == 1:
        #     return 0
        # else:
        #     if nums[1] < nums[0]:
        #         return 0

        #     for idx in range(1, len_nums):
        #         if nums[idx]  < nums[idx - 1]:
        #             return idx - 1

        #     return len_nums - 1

sol = Solution()
# nums = [1, 2, 3, 1]
# nums = [1,2,1,3,5,6,4]
nums = [2, 1, 2]
print(sol.findPeakElement(nums))
