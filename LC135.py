class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        len_ratings = len(ratings)
        candies = [1] * len_ratings

        for idx in range(1, len_ratings):
            if ratings[idx] > ratings[idx - 1]:
                candies[idx] = candies[idx - 1] + 1

        for idx in range(len_ratings - 2, -1, -1):
            if ratings[idx] > ratings[idx + 1]:
                candies[idx] = max(candies[idx], candies[idx + 1] + 1)

        return sum(candies)

        # if not ratings:
        #     return 0

        # len_ratings = len(ratings)

        # if len_ratings == 1:
        #     return 1

        # idx = 1
        # bound = len_ratings - 1
        # res = len_ratings
        # last_have = False

        # if ratings[0] >= ratings[1]:
        #     res += 1
        #     last_have = True

        # while idx < bound:
        #     if ratings[idx - 1] < ratings[idx] >= ratings[idx + 1] or (not last_have and ratings[idx - 1] <= ratings[idx] > ratings[idx + 1]):
        #         res += 1
        #         last_have = True
        #     else:
        #         last_have = False

        #     idx += 1

        # if not last_have and ratings[-1] >= ratings[-2]:
        #     res += 1

        # return res


sol = Solution()
r = [1,0,2]
# r = [1,2,2]
# r = [2, 2]
# r = [0]
# r = [1,3,2,2,1]
# r = [1,2,87,87,87,2,1]
print(sol.candy(r))
