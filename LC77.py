class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        stack = []
        curr = 1
        space = n - k + 1

        while True:
            len_stk = len(stack)

            if len_stk == k or curr > space + len_stk:
                if not stack:
                    return result
                
                if len_stk == k:
                    result.append(stack[:])
                
                curr = stack.pop() + 1
            else:
                stack.append(curr)
                curr += 1

    def combine2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        limit = n + 1
        result = [[num] for num in xrange(1, limit)]

        while k > 1:
            temp_result = []
            k -= 1

            for temp in result:
                temp_result.extend([temp + [num] for num in xrange(temp[-1] + 1, limit)])
            
            result = temp_result

        return result

    def combine3(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.limit = n + 1

        def dfs(temp, cnt):
            if cnt == 0:
                self.result.append(temp)
                return
            else:
                for num in xrange(temp[-1] + 1, self.limit):
                    dfs(temp + [num], cnt - 1)

        for num in xrange(1, self.limit):
            dfs([num], k - 1)

        return self.result


sol = Solution()
print sol.combine3(4, 3)

# from time import time
# t = time()
# sol.combine2(20, 16)
# print time() - t

# t = time()
# print sol.combine3(20, 16)
# print time() - t
        