from itertools import product

class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        groups = [[]]
        level = 0

        for idx, ch in enumerate(expression):
            if ch == '{':
                if level == 0:
                    srt_idx = idx + 1
                
                level += 1
            elif ch == '}':
                level -= 1

                if level == 0:
                    groups[-1].append(self.braceExpansionII(expression[srt_idx: idx]))
            elif level == 0:
                if ch == ',':
                    groups.append([])
                else:
                    groups[-1].append([ch])

        word_set = set()

        for group in groups:
            word_set |= set(map(''.join, product(*group)))
        
        return sorted(word_set)

        # len_exp = len(expression)
        # idx = 0
        # srt_stack = []
        # groups = []

        # while idx < len_exp:
        #     if expression[idx] == '{':
        #         srt_stack.append([idx, True])
        #     elif expression[idx] == '}':
        #         srt_idx, is_new = srt_stack.pop()

        #         if is_new:
        #             temp = expression[srt_idx + 1: idx].split(',')
        #             temp_idx = srt_idx

        #             while temp_idx - 1 > -1 and expression[temp_idx - 1] not in '{,}':
        #                 temp_idx -= 1

        #             temp_pre = expression[temp_idx: srt_idx]

        #             if temp_pre:
        #                 if srt_stack:
        #                     srt_stack[-1][1] = False

        #                 temp = [temp_pre + x for x in temp]

        #             if not groups or temp_idx > 0 and expression[temp_idx - 1] == '{':
        #                 groups.append(set(temp))
        #             elif temp_idx > 0 and expression[temp_idx - 1] == ',':
        #                 groups[-1].update(set(temp))
        #             else:
        #                 groups[-1] = set([a + b for a in groups[-1] for b in temp])

        #     idx += 1

        # if groups:
        #     res = groups[0]

        #     for group in groups[1:]:
        #         res = set([a + b for a in res for b in group])

        #     return sorted(list(res))
        # else:
        #     return [expression]


sol = Solution()
# exp = "{a,b}{c{d,e}}"
exp = "{{a,z},a{b,c},{ab,z}}"
# exp = "{a{b,c}}{{d,e},f{g,h}}"
# exp = "{a,b}{c,d}"
# exp = "abcd"
# exp = "{{a,b},b,c}"
print(sol.braceExpansionII(exp))
