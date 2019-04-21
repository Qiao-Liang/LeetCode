class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        len_weights = len(weights)

        def can_ship(capacity):
            day_count = D
            idx = 0

            while day_count > 0:
                day_count -= 1
                curr_load = 0

                while idx < len_weights and curr_load + weights[idx] <= capacity:
                    curr_load += weights[idx]
                    idx += 1

            return idx == len_weights

        low = 0
        high = sum(weights)

        while high - low > 1:
            mid = (low + high) // 2

            if can_ship(mid):
                high = mid
            else:
                low = mid

        return high


sol = Solution()
# weights = [1,2,3,4,5,6,7,8,9,10]
# D = 5
# weights = [3,2,2,4,1,4]
# D = 3
weights = [1,2,3,1,1]
D = 4
print(sol.shipWithinDays(weights, D))
        