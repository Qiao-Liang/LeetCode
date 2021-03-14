class Solution:
    def maxScoreWords(self, words, letters, score) -> int:
        l = len(words)
        self.res = 0
        b = ord('a')
        
        def dfs(i, t, tc):
            if i < l:
                w = words[i]
                i += 1
                c = [0] * 26
                count_on = True
                add_on = 0
                
                dfs(i, t, tc[:])
                
                for ch in w:
                    ci = ord(ch) - b
                    c[ci] += 1
                    add_on += score[ci]
                
                for ti in range(26):
                    if tc[ti] >= c[ti]:
                        tc[ti] -= c[ti]
                    else:
                        count_on = False
                        break
                
                if count_on:
                    dfs(i, t + add_on, tc[:])
            else:
                self.res = max(self.res, t)
        
        count = [0] * 26
        
        for c in letters:
            count[ord(c) - b] += 1
        
        dfs(0, 0, count)
        return self.res


sol = Solution()
# p = [["dog","cat","dad","good"], ["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]]
p = [["xxxz","ax","bx","cx"], ["z","a","b","c","x","x","x"], [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]]
print(sol.maxScoreWords(*p))
