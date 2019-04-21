class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}  # Tracks the next greater number
        stack = []
        result = []

        for num in nums:
            while stack and stack[-1] < num:
                dic[stack.pop()] = num
            
            stack.append(num)
        
        for num in findNums:
            result.append(dic.get(num, -1))

        return result

    def nextGreaterElement2(self, findNums, nums):
        res = []
        dic = {}

        for idx, n in enumerate(nums):
            dic[n] = idx

        for n in findNums:
            temp = -1

            for temp_n in nums[dic[n] + 1:]:
                if temp_n > n:
                    temp = temp_n
                    break

            res.append(temp)

        return res


sol = Solution()
# findNums = [2, 4]
findNums = [4, 1, 2]
# nums = [1, 2, 3, 4]
nums = [1, 3, 4, 2]

print(sol.nextGreaterElement(findNums, nums))
