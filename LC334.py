class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        poss = [nums[0]]

        for num in nums[1:]:
            idx = 0

            for p in poss:
                if num > p:
                    idx += 1
                else:
                    break

            if idx == 2:
                return True
            elif idx == 1:
                if len(poss) == 2:
                    poss[1] = num
                else:
                    poss.append(num)
            elif idx == 0:
                poss[0] = num

        return False


nums = [1, 2, 3, 4, 5]
# nums = [5, 4, 3, 2, 1]
# nums = [5, 1, 5, 5, 2, 5, 4]
# nums = [10, 12, 7, 8, 1, 2, 3]
# nums = [10, 12, 7, 8, 2, 9]
sol = Solution()
print(sol.increasingTriplet(nums))
