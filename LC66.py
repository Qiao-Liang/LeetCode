"""
Plus one
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        idx = len(digits) - 1
        carry = 0

        while idx > -1:
            digits[idx] += carry

            if digits[idx] > 9:
                digits[idx] %= 10
                carry = 1
            else:
                return digits

            idx -= 1

        return [1] + digits


        # for i in range(len(digits) - 1, -1, -1):
        #     s = digits[i] + 1
            
        #     if s > 9:
        #         digits[i] = 0
        #         if i == 0:
        #             digits.insert(0, 1)
        #     else:
        #         digits[i] += 1
        #         break
        
        # return digits


sol = Solution()
# digits = [1,2,3]
digits = [8, 9, 9]
print(sol.plusOne(digits))
