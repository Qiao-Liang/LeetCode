class Solution:
    def longestSubsequence(self, arr, difference: int) -> int:
        res = {}

        for n in arr:
            temp = n - difference
            res[n] = res[temp] + 1 if temp in res else 1
        
        return max(res.values())

        # len_arr = len(arr)
        # visited = [False] * len(arr)
        # res = 0

        # for l, n in enumerate(arr):
        #     if not visited[l]:
        #         visited[l] = True
        #         r = l + 1
        #         last = n
        #         temp = 1

        #         while r < len_arr:
        #             if arr[r] - last == difference:
        #                 last = arr[r]
        #                 visited[r] = True
        #                 temp += 1

        #             r += 1

        #         res = max(res, temp)

        # return res


        # dic = defaultdict(list)
        # res = 0
        
        # for i, n in enumerate(arr):
        #     dic[n].append(i)
        
        # for i, n in enumerate(arr):
        #     temp = 1
        #     c, ci = n + difference, i
            
        #     while c in dic and ci < dic[c][-1]:
        #         temp += 1
        #         ci = dic[c][bisect_right(dic[c], c) - 1]
        #         c += difference
                
        #     res = max(res, temp)
            
        # return res


sol = Solution()
# p = [[1,2,3,4], 1]
# p = [[1,3,5,7], 1]
p = [[1,5,7,8,5,3,4,2,1], -2]
# p = [[-233,-295,102,473,339,100,350,-338,489,355,196,478,401,364,-62,375,353,-371,272,277,-84,-247,-294,-357,-340,-160,-183,-474,-103,232,-226,210,374,246,-401,279,55,374,182,-28,277,139,469,-208,12,-253,194,-123,191,228,380,-239,401,-425,399,-270,323,-27,84,7,-324,93,-481,-332,387,276,-113,211,277,438,-129,-416,109,157,191,-181,-103,463,-301,-229,158,149,-134,216,370,-78,256,386,-385,428,-57,-222,159,-183,-198,-129,124,-475,-259,-488,-199,-466,-214,41,2,-104,-477,-126,-488,234,-353,425,75,298,70,-132,-356,368,-176,128,491,363,-263,-163,63,70,456,-245,-29,407,337,185,48,-55,-238,79,121,131,-283,320,168,-147,414,-384,146,-386,-275,-178,-140,-198,251,-2,16,-446,219,-269,178,205,-265,253,302,37,43,-444,28,-430,478,90,268,-164,378,107,36,452,-39,452,87,421,-24,-473,486,226,149,-205,394,24,486,13,-333,298,-454,200,-336,67,488,346,-310,-317,428,-311,38,160,-488,-100,434,384,-479,208,48,429,409,369,-164,184,-430,358,-381,376,-267,-413,-430,-247,-277,145,-311,384,460,-282,284,183,-241,312,451,-315,-187,-439,-3,349,78,-319,-429,495,46,-318,-317,326,297,355,-3,-473,-91,191,304,-329,130,-278,-204,-118,-307,-7,359,-258,-123,402,65,-194,-316,-445,400,5,-308,456,-10,42,-23,177,157,-70,-187,340,-432,-170,183,378,166,-456,-462,37,-182,458,-33,450,-1,-373,180,-426,156,-187,169,476,-13,-421,-497,-430,-201,2,173,152,130,-272,394,-295,133,-36,-274,89,-336,-78,-71,460,-280,235,9,-11,-377,-170,56,233,-224,-464,-200,44,447,-432,371,-157,-127,149,-333,-163,474,152,10,-477,165,198,-491,60,206,-259,423,331,231,-366,128,433,486,-44,463,36,480,437,-253,-94,-394,-68,-192,368,72,-69,353,-159,-72,457,385,237,-77,371,-275,383,279,-331,46,344,-283,-70,-454,131,-469,433,-167,177,117,85,293,-415,214,-104,-334,-467,-17,375,290,126,-135,-271,-193,-275,479,-476,-128,387,-85,-195,-436,385,-184,144,-141,-29,-54,-408,230,-250,263,347,483,-272,-177,-449,113,81,-316,-54,445,333,138,-312,414,433,497,86,-120,-324,119,37,-350,323,486,-216,-388,199,46,416,-128,456,-214,83,-353,24,274,37,-26,347,356,-489,398,-32,-251,-210,31,118,-393,407,-29,-359,64,-142,340,334,100,-485,-19,336,-170,139,37,-7,-245,42,-378,87,-182,16,-377,142,-180,277,438,256]
# , -13]
print(sol.longestSubsequence(*p))
