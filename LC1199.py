from heapq import heapify, heappop, heappush

class Solution:
    def minBuildTime(self, blocks, split: int) -> int:
        heapify(blocks)

        while len(blocks) > 1:
            heappop(blocks)
            heappush(blocks, split + heappop(blocks))
        
        return heappop(blocks)

        # blocks.sort()
        # w = 1
        # res = 0

        # while w <= len(blocks):
        #     if w == len(blocks):
        #         res += blocks[-1]
        #         return res
        #     elif w == 1:
        #         w += 1
        #         res += split
        #     else:
        #         res += blocks.pop()
        #         w -= 1

        # return res

        # self.res = 0
        # self.memo = {}

        # def dfs(w, b):
        #     len_b = len(b)

        #     if w >= len_b:
        #         return b[-1]
        #     elif (w, len_b) in self.memo:
        #         return self.memo[(w, len_b)]
        #     elif w == 1:
        #         return split + dfs(2, b)
        #     else:
        #         temp = float('inf')

        #         for i in range(1, w):
        #             temp = min(temp, max(b[-1], dfs(w - i, b[:-i])))

        #         t = self.memo[(w, len_b)] = min(temp, split + min([dfs(w + i, b) for i in range(1, w + 1)]))
        #         return t

        # return dfs(1, blocks)

        # self.memo = {}

        # def recurse(w, b, c):
        #     if (w, b, c) in self.memo:
        #         return self.memo[(w, b, c)]

        #     if w == 0:
        #         return float('inf')
        #     elif w == len(b):
        #         return c + max(b)
        #     else:
        #         t1 = t2 = float('inf')

        #         for i in range(1, len(b)):
        #             t1 = min(t1, recurse(w - 1, b[0: i], c) + recurse(w - 1, b[i:], c))

        #         for i in range(1, w + 1):
        #             t2 = min(t2, recurse(w + i, b, c + i * split))

        #         t = self.memo[(w, b, c)] = min(t1, t2)
        #         return t

        # return recurse(1, blocks, 0)


sol = Solution()
# p = [[1], 1]
# p = [[1,2], 5]
# p = [[1,2,3],1]
p = [[1,1,1,1], 100]
# p = [[84380,69209,11035,55520,85762,85948,16854,47298,57124,23780,98574,31575,9451,59103,15600,97956,12084,34470,76113,70908,47955,84509,13998,64406,31752,290,57883,18703,47025,3569,91383,88996,62191,28941,75169,76573,22708,51657,75037,51980,96031,64801,78516,29582,82926,94049,51566,44588,10778,32281,44433,30849,95904,34783,70262,83942,33375,99869,91656,97051,89760,36932,62402,2651,1790,33619,37214,55731,55918,18484,78986,65622,60972,27051,81435,26922,81214,40161,78190,11903,51448,4179,49791,4766,83032,82815,8409,30946,81909,79694,47847,30857,28132,58614,23087,48595,96156,29246,6208,11552,33485,41899,63692,52846,4474,54006,23575,2929,35279,91972,30516,15325,59503,87777,32451,85109,97180,52741,97816,43460,39150,21179,25640,13966,54919,59150,82562,62621,5866,35697,79795,98985,41098,77074,83813,3505,43707,38206,747,1680,75851,85699,80480,29494,8536,64292,99301,19770,74264,14984,2754,69911,29604,8873,8399,88147,15066,9739,10336,77112,66747,83267,73357,52912,36325,63622,12918,90871,59633,72962,80807,92271,58074,18561,65637,99672,7798,69843,26909,82918,77190,37271,8474,99323,93155,10320,5865,37167,80234,78382,28107,46413,19049,47244,82253,28706,37317,59536,17853,40920,8363,43159,73755,86361,87834,30387,61437,62373,426,97438,56861,34806,68032,31362,18730,79380,85285,92975,61502,30202,40848,47169,61192,90472,55131,13342,92854,51672,70887,12751,6466,37634,49544,77936,79531,4203,7158,49864,36748,41085,49388,36667,30100,98981,10244,34189,23123,21450,71771,59184,14617,58045,21948,69505,4930,37231,60003,74340,89263,7038,72435,53403,5751,66159,37379,5945,13274,932,95506,40691,38817,57236,55658,93199,84170,22138,51971,23524,31966,34767,20519,27776,87552,61159,12268,26097,80485,83916,60067,78343,80759,52516,84679,31740,44335,62894,61949,19767,5072,65213]
# ,98]
print(sol.minBuildTime(*p))
