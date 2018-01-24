class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 0:
            slow = nums[0]
            fast = nums[nums[0]]

            while slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]

            fast = 0
            while slow != fast:
                slow = nums[slow]
                fast = nums[fast]

            return slow

        return -1


sol = Solution()
# m = [n for n in range(1, 10)]
# m.append(2)
# m[3] = 2

# m = [1, 2, 3, 4, 5, 1]
m = [3, 2, 5, 1, 1, 4]

print(sol.findDuplicate(m))
