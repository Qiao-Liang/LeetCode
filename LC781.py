from collections import Counter

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        counter = Counter(answers)
        res = 0

        for key, val in counter.items():
            if key == 0:
                res += val
            else:
                temp = key + 1

                if temp < val:
                    while temp < val:
                        res += temp
                        val -= temp
                    
                    res += key + 1
                elif temp > val:
                    res += temp
                else:
                    res += val

        return res


sol = Solution()
# ans = [1, 1, 1, 0, 0]
ans = [2,1,2,2,2,2,2,2,1,1]
print(sol.numRabbits(ans))
