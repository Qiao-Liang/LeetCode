class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0

        if k > 0:
            set_nums = set(nums)

            for num in set_nums:
                if num + k in set_nums:
                    count += 1

                if num - k in set_nums:
                    count += 1

            count /= 2
        elif k < 0:
            return 0
        else:  
            dict_nums = {}

            for num in nums:
                if num in dict_nums:
                    dict_nums[num] += 1
                else:
                    dict_nums[num] = 1

            for val in dict_nums.values():
                if val > 1:
                    count += 1
        
        return count


sol = Solution()
nums = [3, 1, 4, 1, 5]
# nums = [1, 2, 3, 4, 5]
# nums = [1, 3, 1, 5, 4]
# nums = [1,1,1,2,1]
print sol.findPairs(nums, 2)
        