from collections import defaultdict

class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        res = 0
        pairs = [(v, l) for v, l in zip(values, labels)]
        pairs.sort(key=lambda n: n[0], reverse=True)
        count = defaultdict(int)

        for v, l in pairs:
            if count[l] < use_limit:
                res += v
                count[l] += 1
                num_wanted -= 1

                if num_wanted == 0:
                    break

        return res


# from collections import defaultdict
# from 

# class Solution(object):
#     def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
#         """
#         :type values: List[int]
#         :type labels: List[int]
#         :type num_wanted: int
#         :type use_limit: int
#         :rtype: int
#         """
#         pairs = defaultdict(list)
#         res = 0
        
#         for v, l in zip(values, labels):
#             pairs[l].append(v)
            
#         for l in pairs.keys():
#             pairs[l].sort()
#             pairs[l] = pairs[l][-use_limit:]
            
#         for _ in range(num_wanted):
#             max_val = -float('inf')
#             max_lbl = None
            
#             for l, v in pairs.items():
#                 if v and v[-1] > max_val:
#                     max_val = v[-1]
#                     max_lbl = l
            
#             if pairs[max_lbl]:
#                 res += max_val
#                 pairs[max_lbl].pop()
#             else:
#                 del pairs[max_lbl]
        
#         return res


sol = Solution()
# params = [
#     [9,8,8,7,6]
# ,[0,0,0,1,1]
# ,3
# ,1
# ]
params = [[9,8,8,7,6], [0,0,0,1,1], 3, 2]
print(sol.largestValsFromLabels(*params))
        