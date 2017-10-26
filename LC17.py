class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        dic_nums = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], 
                    '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], 
                    '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        
        result = dic_nums[digits[0]]

        for digit in digits[1:]:
            if digit == '1':
                continue

            temp = []
            for c in dic_nums[digit]:
                temp.extend(map(lambda x: x + c, result))

            result = temp

        return result

sol = Solution()
print(sol.letterCombinations('2319'))
