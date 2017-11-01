class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return None
        if len(nums) == 1:
            return [[nums[0]]]

        result = [[nums[0], nums[1]], [nums[1], nums[0]]]

        for num in nums[2:]:
            group = []
            for elem in result:
                temp = [num] + elem
                bound = len(temp) - 1

                group.append(temp[:])
                for idx in range(0, bound):
                    temp[idx], temp[idx + 1] = temp[idx + 1], temp[idx]
                    group.append(temp[:])
                
            result = group

        return result

sol = Solution()
result = sol.permute([1, 2, 3, 4])

print(result)
