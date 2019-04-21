class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sorted_nums = sorted(nums, reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        dic_rank = {val: str(idx + 1) if idx > 2 else medals[idx] for idx, val in enumerate(sorted_nums)}

        return [dic_rank[num] for num in nums]


sol = Solution()
# nums = [5, 4, 3, 2, 1]
nums = [10,3,8,9,4]
# nums = [1]
print(sol.findRelativeRanks(nums))
