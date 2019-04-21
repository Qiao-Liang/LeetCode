class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        digits = str(N)
        len_digits = len(digits)
        len_cands = len(D)
        res = (len_cands ** len_digits - len_cands) // (len_cands - 1) if len_cands > 1 else len_digits - 1
        poss = len_cands ** (len_digits - 1)

        for idx in range(len_digits):
            res += sum(c < digits[idx] for c in D) * poss

            if digits[idx] not in D:
                return res

            poss //= len_cands

        return res + 1

        # digits = [int(n) for n in str(N)]
        # cands = [int(n) for n in D]
        # len_digits = len(digits)
        # len_cands = len(cands)
        # res = (len_cands ** (len_digits + 1) - len_cands) // (len_cands - 1) if len_cands > 1 else len_digits
        # poss = len_cands ** (len_digits - 1)

        # for num in digits:
        #     res -= sum(n > num for n in cands) * poss
        #     poss //= len_cands

        #     if num not in cands:
        #         break

        # return res


sol = Solution()
# D = ["1","3","5","7"]
# N = 100
# D = ["1","4","9"]
# N = 1000000000
# D = ["3","4","5","6"]
# N = 64
# D = ["3","5","6","7","8"]
# N = 6
D = ["2","3","4","6","8"]
N = 61
# D = ["5","6"]
# N = 19
# D = ["1","7"]
# N = 231
# D = ["1","2","3","4","6","7","9"]
# N = 333
# D = ['7']
# N = 8
# D = ['9']
# N = 555
print(sol.atMostNGivenDigitSet(D, N))
