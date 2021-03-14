class Solution:
    def spellchecker(self, wordlist, queries):
        words_set = set(wordlist)
        words_cap = {}
        words_vow = {}

        def devowel(w):
            return ''.join('*' if c in 'aeiou' else c for c in w)

        def solve(q):
            ql = q.lower()
            qv = devowel(ql)

            if q in words_set:
                return q
            elif ql in words_cap:
                return words_cap[ql]
            elif qv in words_vow:
                return words_vow[qv]
            else:
                return ''

        for w in wordlist:
            wl = w.lower()
            words_cap.setdefault(wl, w)
            words_vow.setdefault(devowel(wl), w)

        return list(map(solve, queries))


sol = Solution()
p = [["KiTe","kite","hare","Hare"], ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]]
# p = [["KiTe","kite","hare","Hare"], ["HARE","keti","keto"]]
print(sol.spellchecker(*p))

# ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
# ['kite', 'kite', 'KiTe', 'Hare', '', '', '', 'kite', '', 'kite']
