class Solution:
    def maxLength(self, arr) -> int:
        self.res = 0
        len_arr = len(arr)

        def dfs(i, cs, l):
            self.res = max(self.res, l)

            if i < len_arr:
                curr = arr[i]
                len_curr = len(curr)
                ts = set(curr)
                i += 1

                if len(ts) == len_curr and len(ts.intersection(cs)) == 0:
                    dfs(i, ts.union(cs), l + len_curr)

                dfs(i, cs, l)
                
        dfs(0, set([]), 0)
        return self.res

    def maxLength2(self, arr) -> int:
        dp = [set()]
        res = 0

        for s in arr:
            ss = set(s)

            if len(ss) == len(s):
                for ps in dp[:]:
                    if not ps & ss:
                        dp.append(ss | ps)
                        res = max(res, len(dp[-1]))
        
        return res


        # len_arr = len(arr)
        # memo = [None] * (len_arr + 1)
        # memo[0] = (0, set([]))
        # res = 0

        # for i in range(1, len_arr + 1):
        #     curr = arr[i - 1]
        #     len_curr = len(curr)
        #     ts = set(curr)

        #     if len_curr == len(ts):
        #         max_len = 0
        #         cs = None

        #         for l, s in memo[:i]:
        #             if len(ts.intersection(s)) == 0 and len_curr + l > max_len:
        #                 max_len = l + len_curr
        #                 cs = ts.union(s)

        #         memo[i] = (max_len, cs)
        #         res = max(res, max_len)
        #     else:
        #         memo[i] = memo[i - 1]

        # print(memo)
        # return res


sol = Solution()
# a = ["un","iq","ue"]
# a = ["cha","r","act","ers"]
# a = ["yy","bkhwmpbiisbldzknpm"]
# a = ["zog","nvwsuikgndmfexxgjtkb","nxko"]
a = ["enrgbdwhqpo","bioedlpz","nfampjeycstxbz","almhiqdypr","qaxldwmgk","mpfgislz","g","yjlipemkuxqsctforbw","udylqhogvfmwikat","euzrimspyfanvlkhb","ltekhadr","wvagsjrzlobm"]

# for i in range(len(a)):
#     for j in range(1 + i, len(a)):
#         if len(a[i]) + len(a[j]) == 20:
#             print(i, j)
#             print(a[i], a[j])

print(sol.maxLength2(a))
