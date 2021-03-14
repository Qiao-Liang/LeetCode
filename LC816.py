class Solution:
    def ambiguousCoordinates(self, s: str):
        res = []
        s = s[1: -1]
        len_s = len(s)
        bound = len_s - 1

        def make_digit(si, ei):
            if s[si] == '0':
                if si == ei:
                    return ['0']
                elif s[ei] == '0':
                    return []

                ni = si + 1

                while ni <= ei and s[ni] == '0':
                    ni += 1

                if ni > ei:
                    return []
                else:
                    return (['0.' + s[si + 1: ei + 1]]) if ei > si else ['0']
            else:
                temp = [s[si: ei + 1]]

                if s[ei] == '0':
                    return temp

                li = ei
                ci = si + 1

                while li > -1 and s[li] == '0':
                    li -= 1

                while ci <= li:
                    temp.append(s[si: ci] + '.' + s[ci: li + 1])
                    ci += 1
                
                return temp
                
        for i in range(len_s - 1):
            l = make_digit(0, i)
            r = make_digit(i + 1, bound)

            if l and r:
                for tl in l:
                    for tr in r:
                        res.append('(' + tl + ', ' + tr + ')')

        return res


sol = Solution()
# s = "(123)"
# s = "(00011)"
# s = "(0123)"
s = "(100)"
# s = "(0010)"
print(sol.ambiguousCoordinates(s))
