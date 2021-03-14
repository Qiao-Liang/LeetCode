class Solution:
    def openLock(self, deadends, target: str) -> int:
        dead_set = set(deadends)

        if '0000' in dead_set:
            return -1
        
        q = ['0000']
        s = 0
        v = set(['0000'])
        cs = '0123456789'
        bi = ord('0')

        while q:
            tq = []

            for c in q:
                if c == target:
                    return s

                l = list(c)

                for i, n in enumerate(l):
                    t = l[:]
                    ni = ord(n) - bi

                    for o in (1, 9):
                        t[i] = cs[(ni + o) % 10]
                        ts = ''.join(t)
                        
                        if ts not in dead_set and ts not in v:
                            v.add(ts)
                            tq.append(ts)

            q = tq
            s += 1
        
        return -1


sol = Solution()
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
# deadends = ["8888"]
# target = "0009"
# deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
# target = "8888"
# deadends = ["0000"]
# target = "8888"

print(sol.openLock(deadends, target))
        