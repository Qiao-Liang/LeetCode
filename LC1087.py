class Solution(object):
    def permute(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        groups = []
        idx = 0
        len_s = len(S)
        res = []
        
        while idx < len_s:
            if S[idx] == "{":
                curr = idx
                
                while curr < len_s and S[curr] != "}":
                    curr += 1
                
                groups.append(S[idx + 1: curr].split(','))
                idx = curr + 1
            else:
                groups.append([S[idx]])
                idx += 1
        
        len_groups = len(groups)
        
        def recurse(idx, temp):
            if idx == len_groups:
                res.append(temp)
            else:
                for ch in groups[idx]:
                    recurse(idx + 1, temp + ch)
                    
        recurse(0, '')
        return res


sol = Solution()
s = "{a,b}c{d,e}f"
print(sol.permute(s))
