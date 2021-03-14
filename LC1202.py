from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs) -> str:
        len_s = len(s)
        sl = list(s)
        visited = [False] * len_s
        g = defaultdict(list)

        for i, j in pairs:
            g[i].append(j)
            g[j].append(i)

        def dfs(i, linked_idx):
            if not visited[i]:
                visited[i] = True
                linked_idx.append(i)
                
                for ni in g[i]:
                    dfs(ni, linked_idx)

        for i in range(len_s):
            linked_idx = []
            dfs(i, linked_idx)
            linked_idx.sort()
            chars = [sl[i] for i in linked_idx]
            chars.sort()

            for i, c in zip(linked_idx, chars):
                sl[i] = c

        return ''.join(sl)

        # p = [(a, b) if a < b else (b, a) for a, b in pairs if a != b]
        # p.sort()
        # last = p[0]
        # pairs = [p[0]]

        # for pair in p[1:]:
        #     if pair != last:
        #         pairs.append(pair)

        #     last = pair

        # self.res = s

        # def dfs(s):
        #     cont = False
                
        #     for ia, ib in pairs:
        #         if s[ia] > s[ib]:
        #             cont = True
        #             s[ia], s[ib] = s[ib], s[ia]
        #             dfs(s[:])
        #             s[ia], s[ib] = s[ib], s[ia]

        #     if not cont:
        #         self.res = min(self.res, ''.join(s))
        
        # dfs(list(s))
        # return self.res


sol = Solution()
# p = ["dcab", [[0,3],[1,2]]]
# p = ["dcab", [[0,3],[1,2], [0, 2]]]
# p = ["cba", [[0, 1], [1, 2]]]
# p = ["qdwyt", [[2,3],[3,2],[0,1],[4,0],[3,2]]]
p = ["udyyek", [[3,3],[3,0],[5,1],[3,1],[3,4],[3,5]]]
print(sol.smallestStringWithSwaps(*p))
