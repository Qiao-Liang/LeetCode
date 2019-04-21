class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        ptrn = [0] * 26
        base = ord('a')
        
        for word in B:
            temp = [0] * 26
            
            for ch in word:
                temp[ord(ch) - base] += 1
                
            for idx in range(26):
                ptrn[idx] = max(ptrn[idx], temp[idx])
        
        res = []
        
        for word in A:
            count = [0] * 26
            to_add = True
            
            for ch in word:
                count[ord(ch) - base] += 1
            
            for idx in range(26):
                if ptrn[idx] > 0 and (count[idx] == 0 or count[idx] < ptrn[idx]):
                    to_add = False
                    break
            
            if to_add:
                res.append(word)
                
        return res


sol = Solution()
A = ["amazon","apple","facebook","google","leetcode"]
# B = ["ec","oc","ceo"]
B = ["e","oo"]
print(sol.wordSubsets(A, B))
