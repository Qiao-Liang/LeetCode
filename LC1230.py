from collections import defaultdict

class Solution:
    def probabilityOfHeads(self, prob, target: int) -> float:
        memo = {0: 1}

        for p in prob:
            temp = defaultdict(int)

            for k in memo:
                temp[k + 1] += memo[k] * p
                temp[k] += memo[k] * (1 - p)

            memo = {k: temp[k] for k in temp if k <= target}

        return memo[target]

        # self.res = []
        # self.memo = set([])
        # coins = len(prob)

        # def recurse(i, p, c):
        #     if (i, p, c) not in self.memo:
        #         self.memo.add((i, p, c))

        #         if i < coins:
        #             cp = prob[i]

        #             if cp == 1:
        #                 recurse(i + 1, p, c + 1)
        #             elif cp == 0:
        #                 recurse(i + 1, p, c)
        #             else:
        #                 recurse(i + 1, p * cp, c + 1)
        #                 recurse(i + 1, p * (1 - cp), c)
        #         else:
        #             if c == target:
        #                 self.res.append(p)

        # recurse(0, 1, 0)
        # return sum(self.res)


sol = Solution()
# p = [[0.4], 0]
# p = [[0.5,0.5,0.5,0.5,0.5], 0]
p = [[0.2,0.8,0,0.3,0.5],3]
# p = [[0.760252208605229,0.9244605121133126,0.9254221563253463,0.028399470765116397,0.9884261977926152,0.5755694375738497,0.5425257378790821,0.10196259097492699,0.8876129137908376,0.21122303112318264,0.8262895102925333,0.9124622052031802,0.031011144788184564,0.38005292182635053,0.07060419063817724,0.669183342731146,0.9768030931640289,0.48908335456130525,0.6229442942842605,0.5778473251852739,0.32556066212136314,0.5562534678009741,0.6771271642465762,0.03737512808588839,0.11874496494010511,0.9280437861535152,0.8912536673221975,0.4388279637720438,0.4327476161174335,0.035169256424374185,0.9045477032822669,0.14600557856950958,0.7752099720592525,0.691855950151288,0.9981892916015322,0.054377473603441695,0.9569455508372251,0.8737251879301638,0.12276270467355699,0.5297807547880916,0.9596827075049228,0.06159341371599214,0.7374299190712934,0.7618178633019035,0.24200248462088414,0.35459059099240264,0.9528609318618948,0.8264012625363151,0.687967807981291,0.4164832753203874],1]
print(sol.probabilityOfHeads(*p))
