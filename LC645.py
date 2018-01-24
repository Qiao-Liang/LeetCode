class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return None

        stat = [0] * (len(nums) + 1)
        result = [0, 0]

        for n in nums:
            stat[n] += 1

        for idx in range(1, len(stat)):
            if stat[idx] == 0:
                result[1] = idx
            if stat[idx] == 2:
                result[0] = idx

        return result


sol = Solution()
print(sol.findErrorNums([1,2,2,4]))
