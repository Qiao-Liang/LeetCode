class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return None
        if len(nums) == 1:
            return [[nums[0]]]

        if nums[0] == nums[1]:
            result = [[nums[0], nums[1]]]
        else:
            result = [[nums[0], nums[1]], [nums[1], nums[0]]]

        for num in nums[2:]:
            group = []
            for elem in result:
                temp = [num] + elem
                bound = len(temp) - 1

                group.append(temp[:])
                for idx in range(0, bound):
                    if temp[idx] == temp[idx + 1]:
                        break

                    temp[idx], temp[idx + 1] = temp[idx + 1], temp[idx]
                    group.append(temp[:])
                
            result = group

        return result


sol = Solution()
result = sol.permuteUnique([1, 1, 2, 2])

print(result)
