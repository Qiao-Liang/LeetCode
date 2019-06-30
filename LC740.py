from collections import Counter

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        last = None
        avoid = using = 0

        for key in sorted(counter.keys()):
            temp = max(avoid, using)

            if key - 1 == last:
                using = key * counter[key] + avoid
                avoid = temp
            else:
                avoid = temp
                using = key * counter[key] + avoid
            
            last = key
        
        return max(avoid, using)

        # if not nums:
        #     return 0

        # dict_nums = {}
        
        # for num in nums:
        #     if num in dict_nums:
        #         dict_nums[num] += 1
        #     else:
        #         dict_nums[num] = 1

        # sorted_keys = sorted(dict_nums.keys())
        # memo = [0] * len(sorted_keys)

        # for idx, key in enumerate(sorted_keys):
        #     if idx == 0:
        #         memo[idx] = key * dict_nums[key]
        #     else:
        #         if key - sorted_keys[idx - 1] > 1:
        #             memo[idx] = key * dict_nums[key] + memo[idx - 1]
        #         else:
        #             memo[idx] = max(memo[idx - 1], (memo[idx - 2] if idx > 1 else 0) + key * dict_nums[key])

        # return memo[-1]


sol = Solution()
# nums = [3, 4, 2]
nums = [2, 2, 3, 3, 3, 4]
# nums = [8,3,4,7,6,6,9,2,5,8,2,4,9,5,9,1,5,7,1,4]
# nums = [3, 3, 3, 4, 2]
# nums = [8,7,3,8,1,4,10,10,10,2]
# nums = [3,7,10,5,2,4,8,9,9,4,9,2,6,4,6,5,4,7,6,10]
# nums = [8,10,4,9,1,3,5,9,4,10]
print(sol.deleteAndEarn(nums))
        