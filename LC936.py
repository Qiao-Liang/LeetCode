class Solution(object):
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        len_stamp = len(stamp)
        len_target = len(target)
        idx = 0
        bound = len_target - len_stamp

        while idx < bound and target[idx: idx + len_stamp] != stamp:
            idx += 1

        res = [idx]
        target = list(target)
        left = idx
        right = idx + len_stamp
        
        for temp_idx in range(idx, idx + len_stamp):
            target[temp_idx] = '?'

        while True:
            max_count = 0
            max_idx = 0
            to_stop = True

            for idx in range(1, len(res)):
                if res[idx] - res[idx] > len_stamp:
                    to_stop = False
                    break
            
            if to_stop and left == 0 and right == len_target:
                break

            for idx in range(len_target - len_stamp + 1):
                count = 0

                for s_idx, t_idx in enumerate(range(idx, idx + len_stamp)):
                    if stamp[s_idx] == target[t_idx]:
                        count += 1

                if count > max_count:
                    max_count = count
                    max_idx = idx

            left = min(left, max_idx)
            right = max(right, max_idx + len_stamp)
            res.append(max_idx)

            for temp_idx in range(max_idx, max_idx + len_stamp):
                target[temp_idx] = '?'

        return res[::-1]


sol = Solution()
# stamp = "abc"
# target = "ababc"
# stamp = "abca"
# target = "aabcaca"
stamp = "oz"
target = "ooozz"
print(sol.movesToStamp(stamp, target))
