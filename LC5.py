class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        temp = ''.join(map(''.join, zip(["#"] * len(s), s)) + ["#"])
        len_temp = len(temp)
        p = [0] * len_temp   # list of the palindrome length at each character
        rb = 0   # right bound
        c = 0   # index of the center point
        max_idx = max_len = 0

        for idx in xrange(1, len_temp):
            p[idx] = min(p[2 * c - idx], rb - idx) if rb > idx else 0

            while idx - p[idx] > 0 and idx + p[idx] + 1 < len_temp and temp[idx - p[idx] - 1] == temp[idx + p[idx] + 1]:
                p[idx] += 1

            if p[idx] > max_len:
                max_len = p[idx]
                max_idx = idx

            if idx + p[idx] > rb:
                rb = idx + p[idx]
                c = idx
        
        return temp[max_idx - max_len:max_idx + max_len + 1].replace("#", '')

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_str = ""
        max_len = 0
        s_len = len(s)

        for head in range(s_len):
            tail = head
            while tail < s_len:
                temp = s[head: tail]
                temp_len = len(temp)

                if temp == temp[::-1] and temp_len > max_len:
                    max_len = temp_len
                    max_str = temp
                
                tail += 1

        return max_str

    def longestPalindrome3(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
        	return ''

        if s == s[::-1]:
            return s
        
        max_len = 1
        start = 0
        for i in xrange(len(s)):
        	if i - max_len >= 1 and s[i - max_len - 1:i + 1] == s[i - max_len - 1:i + 1][::-1]:
        		start = i - max_len - 1
        		max_len += 2
        		continue

        	if i - max_len >= 0 and s[i - max_len:i + 1] == s[i - max_len:i + 1][::-1]:
        		start = i - max_len
        		max_len += 1
        
        return s[start:start + max_len]

sol = Solution()
print(sol.longestPalindrome("babad"))
