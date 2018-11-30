class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        if not haystack:
            return -1

        len_h = len(haystack)
        len_n = len(needle)
        lmt_n = len_n - 1
        fail = [0] * len_n
        curr = 1
        cnt = 0

        while curr < len_n:
            if needle[curr] == needle[cnt]:
                cnt += 1
                fail[curr] = cnt
                curr += 1
            elif cnt > 0:
                cnt = fail[cnt - 1]
            else:
                curr += 1

        curr_n = curr_h = 0

        while curr_h < len_h:
            if haystack[curr_h] == needle[curr_n]:
                if curr_n == lmt_n:
                    return curr_h - lmt_n
                
                curr_h += 1
                curr_n += 1
            elif curr_n > 0:
                curr_n = fail[curr_n - 1]
            else:
                curr_h += 1

        return -1


sol = Solution()
haystack = "aaaaa"
needle = "a m a l g a m a m a i o n".replace(" ", "")

print(sol.strStr(haystack, needle))
