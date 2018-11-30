class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        bound = len(s) + 1
        memo0 = 0
        memo1 = 1
        idx = 1

        while idx < bound:
            temp = 0

            if s[idx - 1] != "0":
                temp = memo1
            
            if idx > 1 and "09" < s[idx - 2: idx] < "27":
                temp += memo0

            memo0 = memo1
            memo1 = temp
            idx += 1
            
        return memo1

        # if not s or s == "0" or "00" in s or s[0] == "0":
        #     return 0

        # bound = len(s)
        # memo = [0] * bound
        # memo[0] = 1
        # idx = 1
        
        # while idx < bound:
        #     if s[idx] == "0":
        #         if int(s[idx - 1]) < 3:
        #             memo[idx] = memo[idx - 2] if idx > 2 else 1
        #         else:
        #             return 0
        #     elif s[idx - 1] == "0":
        #         memo[idx] = memo[idx - 2]
        #     else:
        #         memo[idx] = memo[idx - 1] + (memo[idx - 2] if idx > 2 else 1 if int(s[idx - 1]) * 10 + int(s[idx]) < 27 else 0)
            
        #     idx += 1

        # return memo[-1]


sol = Solution()
print sol.numDecodings("226")
