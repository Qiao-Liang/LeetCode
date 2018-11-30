class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1

        return nums[left]


        # left, right = 0, len(nums) - 1

        # while (right - left > 1):
        #     if nums[left] > nums[right]:
        #         left = (left + right) / 2
        #     else:
        #         left, right = max(left - (right - left), 0), left
        
        # return min(nums[left], nums[right])

    def findMin3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def recurse(nums, left, right):
            if left == right:
                return nums[left]
            
            if right - left == 1:
                return min(nums[left], nums[right])

            mid = (left + right) / 2

            if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                return nums[mid]
            else:
                return min(recurse(nums, mid + 1, right), recurse(nums, left, mid - 1))

        return recurse(nums, 0, len(nums) - 1)

    def findMin2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        left, right = 0, size - 1
        if(nums[left] < nums[right]):
            return nums[left]
        while left + 1 < right:
            mid = (left + right) // 2

            if(nums[mid] > nums[left]):
                left = mid
            elif(nums[mid] < nums[right]):
                right = mid

        if nums[left] < nums[right]:
            return nums[left]
        else:
            return nums[right]


sol = Solution()
nums = [3,4,5,1,2]
# nums = [4,5,6,7,0,1,2]
# nums = [2, 1]
# nums = [2, 3, 1]
print(sol.findMin(nums))
