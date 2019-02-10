class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        temp_sum = sum([num for num in A if not num & 1])
        res = []

        for val, idx in queries:
            old_val = A[idx]

            if not old_val & 1:
                temp_sum -= A[idx]

            A[idx] = old_val + val

            if not A[idx] & 1:
                temp_sum += A[idx]
            
            res.append(temp_sum)

        return res


sol = Solution()
A = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
print(sol.sumEvenAfterQueries(A, queries))
        