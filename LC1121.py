from collections import Counter

class Solution(object):
    def canDivideIntoSubsequences(self, nums, K):
        """
        :type nums: List[int]
        :type K: int
        :rtype: bool
        """
        count = Counter(nums)
        groups = [[] for _ in range(max(count.values()))]
        gi = 0
        len_g = len(groups)

        for n in nums:
            groups[gi].append(n)
            gi = (gi + 1) % len_g

        return min([len(group) for group in groups]) >= K

        # self.res = False
        # len_nums = len(nums)

        # def dfs(nums):
        #     if nums:
        #         temp = []
        #         temp_max = [nums[0]]

        #         for n in nums[1:]:
        #             if n > temp_max[-1]:
        #                 temp_max.append(n)
        #             else:
        #                 temp.append(n)

        #         len_temp_max = len(temp_max)

        #         while len_temp_max >= K:
        #             dfs(temp)




        # self.res = False
        # len_nums = len(nums)
        # visited = set([])

        # def dfs(si):
        #     if si == len_nums:
        #         self.res = True
        #     else:
        #         last = nums[si]
        #         visited.add(si)
        #         temp_len = 1

        #         for i, n in enumerate(nums[si + 1:], start=si + 1):
        #             if i not in visited and n > last:
        #                 temp_len += 1
        #                 last = n
        #                 visited.add(i)

        #                 if temp_len >= K:
        #                     min_i = 0

        #                     while min_i < len_nums and min_i not in visited:
        #                         min_i += 1

        #                     dfs(min_i)

        #                 visited.remove(i)

        #         visited.remove(si)

        # dfs(0)
        # return self.res


sol = Solution()
# nums = [1,2,2,3,3,4,4]
# K = 3
# nums = [5,6,6,7,8]
# K = 3
p = [[1,1,2,3,4,4], 3]

print(sol.canDivideIntoSubsequences(*p))
