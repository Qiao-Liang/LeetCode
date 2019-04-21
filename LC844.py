from itertools import zip_longest

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def iter(s):
            skip = 0

            for c in reversed(s):
                if c == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield c

        for s, t in zip_longest(iter(S), iter(T)):
            if s != t:
                return False

        return True

        # def remove_backspace(text):
        #     idx = len(text) - 1
        #     temp = []
        #     count = 0

        #     while idx > -1:
        #         while idx > -1 and text[idx] == '#':
        #             idx -= 1
        #             count += 1

        #         while idx > -1 and count > 0 and text[idx] != '#':
        #             idx -= 1
        #             count -= 1

        #         if idx > -1 and text[idx] != '#':
        #             temp.append(text[idx])
        #             idx -= 1

        #     return temp

        # return remove_backspace(S) == remove_backspace(T)


sol = Solution()
# S = "ab#c"
# T = "ad#c"
# S = "ab##"
# T = "c#d#"
# S = "a##c"
# T = "#a#c"
# S = "a#c"
# T = "b"
# S = "xywrrmp"
# T = "xywrrmu#p"
S = "bxj##tw"
T = "bxo#j##tw"
# S = "nzp#o#g"
# T = "b#nzp#o#g"
print(sol.backspaceCompare(S, T))
