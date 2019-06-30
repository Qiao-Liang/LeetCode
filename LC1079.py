# from collections import Counter
# from math import factorial

class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        res = {''}

        for c in tiles:
            res |= {d[:i] + c + d[i:] for d in res for i in range(len(d) + 1)}
        
        return len(res) - 1

        # res = 0
        # counts = Counter(tiles).values()
        # prod = 1

        # for count in counts:
        #     prod *= count + 1

        # for i in range(1, prod):
        #     digits = []

        #     for count in counts:
        #         digits.append(i % (count + 1))
        #         i /= count + 1

        #     temp = factorial(sum(digits))
            
        #     for d in digits:
        #         temp /= factorial(d)
            
        #     res += temp
        
        # return res
            