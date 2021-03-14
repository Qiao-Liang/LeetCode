class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        len_clips = len(clips)
        clips.sort(key=lambda n: (n[0], n[1]))
        dp = {}
        si = 0
        res = -1

        while si < len_clips:
            if clips[si][0] == 0:
                dp[clips[si][1]] = 1

                if clips[si][1] >= T:
                    res = 1
            else:
                break

            si += 1

        for i, (s, e) in enumerate(clips[si:],start=si):
            for ts, te in clips[:i]:
                if ts <= s <= te and te in dp:
                    dp[e] = min(dp[e], dp[te] + 1) if e in dp else dp[te] + 1

            if e in dp and e >= T:
                res = dp[e] if res == -1 else min(res, dp[e])
        
        return res

    def videoStitching2(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        len_clips = len(clips)
        clips.sort(key=lambda n: n[0])
        curr_len = res = i = 0

        while i < len_clips:
            temp_len = float('-inf')

            while i < len_clips and curr_len >= clips[i][0]:
                temp_len = max(temp_len, clips[i][0])
                i += 1

            if temp_len == float('-inf'):
                return -1
            else:
                curr_len = temp_len
                res += 1

                if curr_len >= T:
                    return res

        return -1

    def videoStitching3(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        clips.sort(key=lambda n: (n[0], n[1]))
        len_clips = len(clips)
        memo = [0] * (len_clips + 1)
        
        if clips[0][0] > 0 or clips[-1][1] < T:
            return -1

        def dfs(idx):
            if clips[idx][1] >= T:
                return 1

            if not memo[idx]:
                res = len_clips - idx

                for next_idx in range(idx + 1, len_clips):
                    if clips[next_idx][0] <= clips[idx][1]:
                        res = min(res, dfs(next_idx))
                    else:
                        break

                memo[idx] = res + 1

            return memo[idx]

        return min([dfs(idx) for idx in range(len_clips - 1) if clips[idx][0] == 0])


sol = Solution()
clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
T = 10
# clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]]
# T = 9
# clips = [[0,4],[2,8]]
# T = 5
print(sol.videoStitching(clips, T))
