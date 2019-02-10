class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        dic = {}
        visited = set([])

        for idx, num in enumerate(nums):
            dic[num] = idx
        
        for idx in range(len(nums)):
            if idx not in visited:
                temp = nums[idx]
                temp_set = set([])
                temp_count = 0
                visited.add(idx)

                while temp not in temp_set:
                    visited.add(temp)
                    temp_set.add(temp)
                    temp_count += 1
                    temp = nums[temp]


                res = max(res, temp_count)

        return res


sol = Solution()
A = [5,4,0,3,1,6,2]
print(sol.arrayNesting(A))
        