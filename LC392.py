from collections import defaultdict
from bisect import bisect_left

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = defaultdict(list)
        low = 0
        
        for idx, ch in enumerate(t):
            dic[ch].append(idx)

        for ch in s:
            if ch not in dic:
                return False

            indices = dic[ch]
            idx = bisect_left(indices, low)

            if idx == len(indices):
                return False
            
            low = indices[idx] + 1
        
        return True


        # if not s:
        #     return True

        # if not t:
        #     return False

        # s_idx = t_idx = 0
        # len_s = len(s)
        # len_t = len(t)

        # while s_idx < len_s:
        #     while t_idx < len_t and s[s_idx] != t[t_idx]:
        #         t_idx += 1
            
        #     if t_idx == len_t:
        #         return False
            
        #     t_idx += 1
        #     s_idx += 1
        
        # return True


        # if not s:
        #     return True

        # if not t:
        #     return False

        # len_s = len(s)
        # len_t = len(t)
        # memo = [[False] * len_t for _ in range(len_s)]
        # memo[0][0] = s[0] == t[0]

        # for t_idx in range(1, len_t):
        #     memo[0][t_idx] = memo[0][t_idx - 1] or t[t_idx] == s[0]
        
        # if memo[0][-1] == False:
        #     return False

        # srt_idx = 2

        # for s_idx in range(1, len_s):
        #     temp_idx = None

        #     for t_idx in range(srt_idx, len_t):
        #         memo[s_idx][t_idx] = memo[s_idx - 1][t_idx] and (memo[s_idx][t_idx - 1] or s[s_idx] == t[t_idx])
                
        #         if not temp_idx and memo[s_idx][t_idx]:
        #             temp_idx = t_idx

        #     if memo[s_idx][-1] == False:
        #         return False

        #     srt_idx = temp_idx + 1

        # return memo[-1][-1]


sol = Solution()
# s = "abc"
# t = "ahbgdc"
# s = "axc"
# t = "ahbgdc"
# s = ""
# t = "ahbgdc"
# s = "abc"
# t = ""
s = "acb"
t = "ahbgdc"
print(sol.isSubsequence(s, t))
