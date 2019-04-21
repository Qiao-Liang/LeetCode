class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        memo = A[:]
        sums = A[:]
        avg = {}
        len_a = len(A)
        srt_idx = 1

        for idx in range(1, len_a):
            sums[idx] += sums[idx - 1]
            memo[idx] = float(sums[idx]) / (idx + 1)

        def get_avg(last_idx, curr_idx):
            if (last_idx, curr_idx) in avg:
                return avg[last_idx, curr_idx]
            else:
                temp_avg = float(sums[curr_idx] - sums[last_idx]) / (curr_idx - last_idx)
                avg[last_idx, curr_idx] = temp_avg
                return temp_avg


        while srt_idx < K:
            temp_memo = memo[:]

            for curr_idx in range(srt_idx, len_a):
                temp_memo[curr_idx] = max([memo[last_idx] + get_avg(last_idx, curr_idx) for last_idx in range(curr_idx)])

            srt_idx += 1
            memo = temp_memo

        return memo[-1]


        # memo = A[:]
        # temp_len = 2
        # len_A = len(A)
        # avgs = [[None] * len_A for _ in range(len_A)]

        # for r in range(len_A):
        #     avgs[r][r] = A[r]

        #     for c in range(r + 1, len_A):
        #         avgs[r][c] = avgs[r][c - 1] + A[c]

        # for r in range(len_A):
        #     for c in range(r + 1, len_A):
        #         avgs[r][c] /= (c + 1 - r)

        # for idx in range(1, len_A):
        #     memo[idx] = memo[idx - 1] + A[idx]

        # for idx in range(1, len_A):
        #     memo[idx] /= temp_len
        #     temp_len += 1

        # for srt_idx in range(1, K):
        #     temp_memo = [0] * len_A

        #     for temp_idx in range(srt_idx, len_A):
        #         for idx in range(srt_idx - 1, temp_idx):
        #             temp_memo[temp_idx] = max(memo[idx] + avgs[idx + 1][temp_idx], temp_memo[temp_idx])

        #     memo = temp_memo

        # return memo[-1]


        # self.length = len(A)
        # self.avgs = [[None] * self.length for _ in range(self.length)]
        # self.res = 0

        # for r in range(self.length):
        #     self.avgs[r][r] = A[r]

        #     for c in range(r + 1, self.length):
        #         self.avgs[r][c] = self.avgs[r][c - 1] + A[c]

        # for r in range(self.length):
        #     for c in range(r + 1, self.length):
        #         self.avgs[r][c] /= (c + 1 - r)

        # def dfs(srt_idx, grp_cnt, temp):
        #     if grp_cnt == K:
        #         self.res = max(self.res, sum(temp) + self.avgs[srt_idx][self.length - 1])
        #         return

        #     grp_cnt += 1

        #     for idx in range(srt_idx, self.length):
        #         if idx == self.length - 1:
        #             self.res = max(self.res, self.avgs[srt_idx][idx])
        #         else:
        #             temp.append(self.avgs[srt_idx][idx])
        #             dfs(idx + 1, grp_cnt, temp)
        #             temp.pop()

        # dfs(0, 1, [])
        # return self.res


sol = Solution()
A = [9,1,2,3,9]
K = 3
# A = [1,2,3,4,5,6,7]
# K = 4
print(sol.largestSumOfAverages(A, K))
