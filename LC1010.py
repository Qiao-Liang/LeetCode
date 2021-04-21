from collections import Counter

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        counts = Counter()
        res = 0

        for t in time:
            res += counts[-t % 60]
            counts[t % 60] += 1

        return res

        # counts = Counter([tm % 60 for tm in time])
        # temp = counts[0]
        # temp -= 1
        # res = 0

        # while temp > 0:
        #     res += temp
        #     temp -= 1

        # for key in counts:
        #     pair_key = 60 - key

        #     if key != 0 and pair_key in counts:
        #         if pair_key == key:
        #             temp = counts[key]
        #             temp -= 1

        #             while temp > 0:
        #                 res += temp
        #                 temp -= 1
                    
        #             counts[key] = 0
        #         else:
        #             res += counts[key] * counts[pair_key]
        #             counts[key] = 0
        #             counts[pair_key] = 0

        # return res


sol = Solution()
# time = [60,60,60]
time = [30,20,150,100,40]
# time = [20, 40]
# time = [418,204,77,278,239,457,284,263,372,279,476,416,360,18]
# time = [269,230,318,468,171,158,350,60,287,27,11,384,332,267,412,478,280,303,242,378,129,131,164,467,345,146,264,332,276,479,284,433,117,197,430,203,100,280,145,287,91,157,5,475,288,146,370,199,81,428,278,2,400,23,470,242,411,470,330,144,189,204,62,318,475,24,457,83,204,322,250,478,186,467,350,171,119,245,399,112,252,201,324,317,293,44,295,14,379,382,137,280,265,78,38,323,347,499,238,110,18,224,473,289,198,106,256,279,275,349,210,498,201,175,472,461,116,144,9,221,473]
# time = [309,148,402,199,180,170,293,72,165,318,178,444,105,265,311,223,242,11,341,232,37,90,214,73,15,431,82,323,291,296,234,32,21,156,235,379,275,273,69,91,275,93,281,212,478,365,126,457,268,85,217,144,325,376,357,457,129,189,140,384,21,342,416,34,252,216,311,228,380,149,123,276,458,225,271,489,125,377,440,459,428,52,372,337,55,1,183,214,42,174,193,196,230,144,213,292,34,8,61,432,23,24,128,416,136,196,290,406,103,394,408,97,222,418,122,94,171,214,418,458,141,356,212,217,428,183,488,471,29,441,190,133,152,448,390,40,180,28,156,43,299,251,250,48,423,437,417,303,81,284,448,459,30,273,141,111,61,366,157,434,155,114,208,423,56,8,95,461,351,448,244,244,121,112,374,267,26,176,203,24,142,98,372,208,438,335,432,456,161,157,353,161,235,395,389,208]
print(sol.numPairsDivisibleBy60(time))
        