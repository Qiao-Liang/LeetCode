class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ch_counts = {}
        res = 0
        odds = []

        for ch in s:
            if ch in ch_counts:
                ch_counts[ch] += 1
            else:
                ch_counts[ch] = 1
        
        for count in ch_counts.values():
            if count & 1:
                odds.append(count)
            else:
                res += count

        if odds:
            odds = sorted(odds, reverse = True)

            res += odds[0]

            for odd in odds[1:]:
                res += odd - 1

        return res

        # len_s = len(s)

        # def recurse(s, max_len, left, right):
        #     if left == right:
        #         return 1
            
        #     if left > right:
        #         return 0

        #     if max_len[left][right] == -1:
        #         if s[left] == s[right]:
        #             max_len[left][right] = 2 + recurse(s, max_len, left + 1, right - 1)
        #         else:
        #             max_len[left][right] = max(recurse(s, max_len, left + 1, right), recurse(s, max_len, left, right - 1))
            
        #     return max_len[left][right]

        # return recurse(s, [[-1] * len_s for _ in xrange(len_s)], 0, len_s - 1)


sol = Solution()
print sol.longestPalindrome("bb")
