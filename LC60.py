class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        temp = [0] * n
        perm = 1

        for i in xrange(0, n):
            temp[i] = i + 1
            perm *= temp[i]

        perm /= n

        def recurse(temp, k, srt, perm):
            if k == 1:
                return temp

            if k == 2:
                temp[-1], temp[-2] = temp[-2], temp[-1]

                return temp

            counts = (k - 1) / perm
            temp_idx = counts + srt
            temp.insert(srt, temp.pop(temp_idx))
            new_k = k - perm * counts
            perm = perm / (n - srt - 1)

            return recurse(temp, new_k, srt + 1, perm)

        result = recurse(temp, k, 0, perm)

        return ''.join([str(i) for i in result])


sol = Solution()
print sol.getPermutation(3, 5)
