from collections import Counter

class Solution:
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A:
            return True

        counter = Counter(A)
        keys = list(counter.keys())
        keys.sort()

        for num in keys:
            if num == 0:
                if counter[num] & 1:
                    return False
                else:
                    counter[num] = 0

            target = num * 2

            if target in counter:
                temp = min(counter[num], counter[target])
                counter[num] -= temp
                counter[target] -= temp

        return len([key for key in keys if counter[key] > 0]) == 0

        # counter = Counter(A)

        # for num in counter.keys():
        #     if num == 0:
        #         if counter[num] & 1:
        #             return False
        #         else:
        #             counter[num] = 0

        #     target = num * 2

        #     if target in counter:
        #         temp = min(counter[num], counter[target])
        #         counter[num] -= temp
        #         counter[target] -= temp

        # return len([key for key in counter.keys() if counter[key] > 0]) == 0


sol = Solution()
# a = [4,-2,2,-4]
# a = [2,1,2,6]
# a = [4,-3,2,-4]
# a = [2,-1,1,4,-2,4]
# a = [2,1,2,1,1,1,2,2]
# a = [-8,-4,-2,-1,0,0,1,2,4,8]
# a = [-6, -3]
# a = [0, 0]
# a = [-2,-6,-3,4,-4,2]
a = [-6,2,-6,4,-3,8,3,2,-2,6,1,-3,-4,-4,-8,4]
print(sol.canReorderDoubled(a))
        