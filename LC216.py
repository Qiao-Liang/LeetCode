class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = []

        def recurse(curr_num, curr_list, k, n):
            curr_list.append(curr_num)

            if len(curr_list) == k:
                if sum(curr_list) == n:
                    self.res.append(curr_list[:])
            else:
                if sum(curr_list) < n:
                    for next_num in xrange(curr_num + 1, 10):
                        recurse(next_num, curr_list, k, n)
                        curr_list.pop()

        for num in xrange(1, 10):
            recurse(num, [], k, n)

        return self.res

        # stack = []
        # res = []
        # curr = 1

        # while True:
        #     if len(stack) == k:
        #         if sum(stack) == n:
        #             res.append(stack[:])
                
        #         curr = stack.pop() + 1
        #     elif len(stack) == 1:
        #         if stack[0] == 9:
        #             break
        #     else:
        #         if curr == 10:
        #             curr = stack.pop() + 1

        #             if not stack:
        #                 break
        #         else:
        #             stack.append(curr)
        #             curr += 1

        # return res


sol = Solution()
k = 3
n = 9
print sol.combinationSum3(k, n)
