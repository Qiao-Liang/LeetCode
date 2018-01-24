class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        freq = {}

        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        return ''.join([elem[0] * elem[1] for elem in sorted(freq.items(), key=lambda x:x[1], reverse=True)])


sol = Solution()
print(sol.frequencySort('tree'))
