class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        self.memo = {}
        
        def recurse(s, e):
            if (s, e) in self.memo:
                return self.memo[s, e]
            
            if s == e:
                return 0, arr[s]
            elif e - s == 1:
                temp = (arr[s] * arr[e], max(arr[s], arr[e]))
                self.memo[s, e] = temp
                return temp
            else:
                min_sum = float('inf')
                max_val = float('-inf')
                
                for m in range(s, e):
                    lp, lm = recurse(s, m)
                    rp, rm = recurse(m + 1, e)
                    max_val = max(max_val, lm, rm)
                    min_sum = min(min_sum, lp + rp + lm * rm)
                
                self.memo[s, e] = (min_sum, max_val)
                return (min_sum, max_val)
                
        return recurse(0, len(arr) - 1)[0]


sol = Solution()
# arr = [6,2,4]
arr = [7,12,8,10]
print(sol.mctFromLeafValues(arr))
