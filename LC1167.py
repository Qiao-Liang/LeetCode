from heapq import heapify, heappush, heappop

class Solution:
    def connectSticks(self, sticks) -> int:
        res = 0
        heapify(sticks)

        while len(sticks) > 1:
            temp = heappop(sticks) + heappop(sticks)
            res += temp
            heappush(sticks, temp)

        return res

sol = Solution()
# s = [2, 4, 3]
# s = [1, 8, 3, 5]
s = [1175,8967,1382,8748,8612,7067,5979,8237,9691,389,5801,7387,8620,6674,1610,7444,6969,970,9463,7727,5044,1834,3426,3192,9473,2300,3647,6492,3166,3486,454,6077,670,4929,1266,8288,8554,8432,4724,8553,2442,1776,2704,1276,2933,3376,8259,8548,1563,3884]
print(sol.connectSticks(s))
