from collections import Counter

class Solution(object):
    def numKLenSubstrNoRepeats(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: int
        """
        l = 0
        r = K
        bound = len(S)
        res = []

        while r <= bound:
            if len(set(S[l: r])) == K:
                res.append(S[l: r])

            l += 1
            r += 1

        return res

        # while idx < bound:
        #     temp_idx = idx

        #     while count > 0:
        #         if S[temp_idx] in temp:
        #             idx = temp[S[temp_idx]]
        #             temp = {S[idx]: idx}
        #             break
        #         else:
        #             temp[S[temp_idx]] = temp_idx
        #             temp_idx += 1
        #             count -= 1
                    
        #             if count == 0:
        #                 res.append(S[idx: temp_idx + 1])
        #                 idx += 1
        #                 break
            
        # return res


sol = Solution()
params = ["havefunonleetcode", 5]
print(sol.numKLenSubstrNoRepeats(*params))
        