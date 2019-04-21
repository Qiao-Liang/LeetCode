class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        res = [None] * len(queries)
        len_ptn = len(pattern)

        for idx, query in enumerate(queries):
            p_idx = 0

            for c in query:
                if p_idx < len_ptn and c == pattern[p_idx]:
                    p_idx += 1
                elif c.isupper():
                    res[idx] = False
                    break
            else:
                res[idx] = p_idx == len_ptn

        return res

        # list_ptn = []
        # res = []
        
        # for idx, ch in enumerate(pattern):
        #     if ch.isupper():
        #         list_ptn.append(idx)

        # if not list_ptn:
        #     return [False] * len(queries)
                
        # for idx in range(len(list_ptn) - 1):
        #     list_ptn[idx] = pattern[list_ptn[idx]: list_ptn[idx + 1]]
        
        # list_ptn[-1] = pattern[list_ptn[-1]:]
        # len_list = len(list_ptn)
        
        # for query in queries:
        #     p_idx = 0
        #     p_len = len(list_ptn[p_idx])
        #     res.append(True)
        #     upper_count = 0
            
        #     for q_idx, q_ch in enumerate(query):
        #         if q_ch.isupper():
        #             upper_count += 1

        #             if upper_count > len_list:
        #                 res[-1] = False
        #                 break

        #             if q_ch == list_ptn[p_idx][0] and query[q_idx: q_idx + p_len] == list_ptn[p_idx]:
        #                 p_idx += 1
                        
        #                 if p_idx < len_list:
        #                     p_len = len(list_ptn[p_idx])
        #             else:
        #                 res[-1] = False
        #                 break

        #     if upper_count < len_list:
        #         res[-1] = False

        # return res


sol = Solution()
q = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
p = "FB"
# q = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
# p = "FoBa"
# q = ["mifeqvzphnrv","mieqxvrvhnrv","mhieqovhnryv","mieqekvhnrpv","miueqrvfhnrv","mieqpvhzntrv","gmimeqvphnrv","mieqvhqyunrv"]
# p = "mieqvhnrv"
# q = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
# p = "FoBaT"
print(sol.camelMatch(q, p))
