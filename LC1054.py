from collections import Counter

class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        counter = [[num, count] for num, count in Counter(barcodes).items()]
        counter.sort(key=lambda n: n[1], reverse=True)
        len_bar = len(barcodes)
        res = [0] * len_bar
        idx = 0

        for k, v in counter:
            for _ in range(v):
                res[idx] = k
                idx += 2

                if idx >= len_bar:
                    idx = 1

        return res

        # while go_on:
        #     temp = 0

        #     for num in counter.keys():
        #         if counter[num] and num != res[idx - 1]:
        #             temp += 1

        #             if temp == 2:
        #                 break

        #             res[idx] = num
        #             idx += 1
        #             counter[num] -= 1

        #             if idx == len_bar:
        #                 go_on = False
        #                 break

        # return res


sol = Solution()
# c = [1,1,1,2,2,2]
# c = [1,1,1,1,2,2,3,3]
c = [2,2,2,1,5]
# c = [2,1,1]
print(sol.rearrangeBarcodes(c))
