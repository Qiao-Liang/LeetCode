class Solution:
    def canMakePaliQueries(self, s: str, queries):
        res = [None] * len(queries)

        for i, (l, r, k) in enumerate(queries):
            if l == r:
                res[i] = True
            else:
                c = 0
                tl = l
                tr = r

                while tl <= tr:
                    if s[tl] == s[tr]:
                        c += 1
                    
                    tl += 1
                    tr -= 1

                length = r - l + 1

                if length & 1:
                    c -= 1

                res[i] = length // 2 - c <= k

        return res


sol = Solution()
# p = ["abcda", [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]]
# p = ["rkzavgdmdgt", [[5,8,0],[7,9,1],[3,6,4],[5,5,1],[8,10,0],[3,9,5],[0,10,10],[6,8,3]]]
p = ["hunu",[[1,1,1],[2,3,0],[3,3,1],[0,3,2],[1,3,3],[2,3,1],[3,3,1],[0,3,0],[1,1,1],[2,3,0],[3,3,1],[0,3,1],[1,1,1]]]
print(sol.canMakePaliQueries(*p))
