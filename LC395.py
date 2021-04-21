class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        dic = {}
        
        for i, n in enumerate(s):
            if n in dic:
                dic[n][1] = i
                dic[n][2] += 1
            else:
                dic[n] = [i, i, 1]
                
        intervals = [(s, e) for s, e, n in dic.values() if n >= k]
        intervals.sort(key=lambda n: n[1])
        
        ls, le = intervals[0]
        res = le - ls + 1

        for s, e in intervals[1:]:
            if s < le or s - le == 1:
                le = e
            else:
                res = max(res, le - ls + 1)
                ls, le = s, e
        
        return max(res, le - ls + 1)


sol = Solution()
# s = "ababbc"
# k = 2
p = ("aaabbb", 3)
print(sol.longestSubstring(*p))
