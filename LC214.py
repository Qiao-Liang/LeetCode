class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        len_s = len(s)
        lmt_s = len_s - 1
        curr = 1
        cnt = 0
        fail = [0] * len_s
        rev_s = s[::-1]

        while curr < len_s:
            if s[curr] == s[cnt]:
                cnt += 1
                fail[curr] = cnt
                curr += 1
            elif cnt > 0:
                cnt = fail[cnt - 1]
            else:
                curr += 1

        curr = curr_rev = 0
        temp = 0

        while curr < len_s:
            if s[curr] == rev_s[curr_rev]:
                if curr_rev == lmt_s:
                    temp = lmt_s - curr
                    break

                curr += 1
                curr_rev += 1
            elif curr > 0:
                curr = fail[curr - 1]
            else:
                curr_rev += 1

        return rev_s[:temp] + s


sol = Solution()
print(sol.shortestPalindrome("abb"))
# print(sol.shortestPalindrome("aaacecaa"))
