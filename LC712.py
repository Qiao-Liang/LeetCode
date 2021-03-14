class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        len1, len2 = len(s1), len(s2)
        memo = [[(0, 0)] * (len2 + 1) for _ in range(len1 + 1)]
        total_ascii = 0
        max_len = 0
        max_ascii = 0

        for c in s1:
            total_ascii += ord(c)

        for c in s2:
            total_ascii += ord(c)

        for i1 in range(1, len1 + 1):
            for i2 in range(1, len2 + 1):
                if s1[i1 - 1] == s2[i2 - 1]:
                    memo[i1][i2] = (memo[i1 - 1][i2 - 1][0] + 1, memo[i1 - 1][i2 - 1][1] + ord(s1[i1 - 1]))
                else:
                    if memo[i1 - 1][i2][0] > memo[i1][i2 - 1][0]:
                        memo[i1][i2] = memo[i1 - 1][i2]
                    elif memo[i1 - 1][i2][0] < memo[i1][i2 - 1][0]:
                        memo[i1][i2] = memo[i1][i2 - 1]
                    else:
                        if memo[i1 - 1][i2][1] > memo[i1][i2 - 1][1]:
                            memo[i1][i2] = memo[i1 - 1][i2]
                        else:
                            memo[i1][i2] = memo[i1][i2 - 1]
                
                if memo[i1][i2][0] >= max_len:
                    max_len = memo[i1][i2][0]
                    max_ascii = max(max_ascii, memo[i1][i2][1])

        return total_ascii - (max_ascii << 1)


sol = Solution()
# params = ["sea", "eat"]
params = ["delete", "leet"]
print(sol.minimumDeleteSum(*params))
