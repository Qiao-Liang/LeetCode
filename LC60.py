class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        temp = [num for num in range(1, n + 1)]
        perm = 1
        srt = 0
        
        for num in temp[1: -1]:
            perm *= num

        while k > 0:
            if k == 1:
                break

            if k == 2:
                temp[-1], temp[-2] = temp[-2], temp[-1]
                break
            
            counts = (k - 1) // perm
            temp_idx = counts + srt

            while temp_idx > srt:
                temp[temp_idx], temp[temp_idx - 1] = temp[temp_idx - 1], temp[temp_idx]
                temp_idx -= 1

            k -= perm * counts
            perm //= (n - srt - 1)
            srt += 1
        
        return ''.join(map(str, temp))


        # temp = [0] * n
        # perm = 1

        # for i in range(0, n):
        #     temp[i] = i + 1
        #     perm *= temp[i]

        # perm //= n

        # def recurse(temp, k, srt, perm):
        #     if k == 1:
        #         return temp

        #     if k == 2:
        #         temp[-1], temp[-2] = temp[-2], temp[-1]

        #         return temp

        #     counts = (k - 1) // perm
        #     temp_idx = counts + srt
        #     temp.insert(srt, temp.pop(temp_idx))
        #     new_k = k - perm * counts
        #     perm = perm // (n - srt - 1)

        #     return recurse(temp, new_k, srt + 1, perm)

        # result = recurse(temp, k, 0, perm)

        # return ''.join([str(i) for i in result])


sol = Solution()
print(sol.getPermutation(4, 9))
