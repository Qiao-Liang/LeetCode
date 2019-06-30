class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        res = 0
        len_cus = len(customers)
        l_sum = 0
        r_sum = sum([n for idx, n in enumerate(customers[X:], start=X) if grumpy[idx] == 0])
        curr_sum = sum(customers[:X - 1])
        last = 0
        
        for idx in range(len_cus - X + 1):
            r_idx = idx + X - 1
            curr_sum += customers[r_idx]
            curr_sum -= last
            res = max(res, l_sum + r_sum + curr_sum)
            l_sum += customers[idx] if grumpy[idx] == 0 else 0
            last = customers[idx]
            r_idx += 1
            
            if r_idx < len_cus:
                r_sum -= customers[r_idx] if grumpy[r_idx] == 0 else 0
            
        return res


sol = Solution()
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
X = 3
print(sol.maxSatisfied(customers, grumpy, X))
