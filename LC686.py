class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        idx_a = idx_b = idx_srt = 0
        len_a = len(A)
        len_b = len(B)
        count = 1

        while True:
            if A[idx_a] == B[idx_b]:
                idx_a += 1
                idx_b += 1
            else:
                idx_srt = (idx_srt + 1) % len_a

                if idx_srt == 0:
                    return -1
                
                idx_a = idx_srt
                idx_b = 0

            if idx_b == len_b - 1:
                return count

            if idx_a == len_a:
                count += 1
                idx_a = 0


sol = Solution()
A = "abcd"
B = "cdabcdab"
# A = "a"
# B = "aa"
# A = "a"
# B = "a"
# A = "aa"
# B = "a"
# A = "aaac"
# B = "aac"
# A = "aabaa"
# B = "aaab"
print(sol.repeatedStringMatch(A, B))
