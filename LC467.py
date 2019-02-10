class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        if not p:
            return 0

        count = [0] * 26
        max_len = 1
        base = ord('a')
        count[ord(p[0]) - base] = 1
        prev = ord(p[0])
        
        for idx in range(1, len(p)):
            curr = ord(p[idx])
            max_len = max_len + 1 if (curr - prev) % 26 == 1 else 1       
            temp_idx = curr - base
            count[temp_idx] = max(count[temp_idx], max_len)
            prev = curr

        return sum(count)

        # if not p:
        #     return 0

        # len_p = len(p)
        # idx = 0
        # global_set = set([])

        # while idx < len_p:
        #     temp_idx = idx
        #     temp_set = set([])

        #     while True:
        #         temp_set.add(p[temp_idx])
        #         temp_idx += 1
                
        #         if temp_idx < len_p:
        #             diff = ord(p[temp_idx]) - ord(p[temp_idx - 1])

        #             if diff == 1 or diff == -25:
        #                 temp = map(lambda x: x + p[temp_idx], list(temp_set))
        #                 temp_set.update(temp)
        #             else:
        #                 break
        #         else:
        #             break

        #     global_set.update(temp_set)
        #     idx = temp_idx

        # return len(temp_set)


sol = Solution()
p = 'zab'
# p = "abaab"
# p = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
print(sol.findSubstringInWraproundString(p))
