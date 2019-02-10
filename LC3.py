class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        len_s = len(s)
        dist = set([])
        left = right = 0
        res = 0
        dist.add(s[0])

        while right + 1 < len_s:
            right += 1

            while left < right and s[right] in dist:
                dist.remove(s[left])
                left += 1

            dist.add(s[right])
            res = max(res, right - left)

        return res + 1


sol = Solution()
s = ""
print(sol.lengthOfLongestSubstring(s))
        