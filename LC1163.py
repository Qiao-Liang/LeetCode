class Solution:
    def lastSubstring(self, s: str) -> str:
        len_s = len(s)
        gi, indices = 0, list(range(len_s))

        while len(indices) > 1:
            temp = []
            max_char = max([s[gi + i] for i in indices if i + gi < len_s])

            for i, v in enumerate(indices):
                if i > 0 and indices[i - 1] + gi == v:
                    continue
                elif gi + v >= len_s:
                    break
                elif s[gi + v] == max_char:
                    temp.append(v)

            gi += 1
            indices = temp
        
        return s[indices[0]:]


sol = Solution()
s = "abab"
print(sol.lastSubstring(s))
