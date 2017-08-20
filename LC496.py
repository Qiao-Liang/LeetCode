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


sol = Solution()
# findNums = [2, 4]
findNums = [4, 1, 2]
# nums = [1, 2, 3, 4]
nums = [1, 3, 4, 2]

print(sol.nextGreaterElement(findNums, nums))
