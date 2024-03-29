class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0 
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] > target:
                if target == nums[start]:
                    return start
                elif nums[start] < target or nums[mid] < nums[end]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] < target:
                if target == nums[end]:
                    return end
                elif target < nums[end] or nums[start] < nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                return mid

        return -1


sol = Solution()
# nums = [1]
# nums = [5, 6, 7, 0, 1, 2, 4]
nums = [3, 5, 1]
print(sol.search(nums, 5))
