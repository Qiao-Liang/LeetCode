class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        sk_idx = {v: i for i, v in enumerate(req_skills)}
        dp = {0: []}

        for i, p in enumerate(people):
            sks = 0

            for sk in p:
                if sk in sk_idx:
                    sks |= 1 << sk_idx[sk]
            
            for k, v in list(dp.items()):
                incld = k | sks

                if incld != k and (incld not in dp or len(dp[incld]) > len(v) + 1):
                    dp[incld] = v + [i]

        return dp[(1 << len(req_skills)) - 1]


    def smallestSufficientTeam2(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        len_ppl = len(people)
        self.res = [i for i in range(len_ppl)]
        
        def recurse(pi, sks, ppl):
            temp = set([])
            ppl.append(pi)
            
            for sk in people[pi]:
                if sk in sks:
                    temp.add(sk)
                    sks.remove(sk)
            
            if len(sks) == 0:
                if len(ppl) < len(self.res):
                    self.res = ppl[:]
            else:
                for npi in range(pi + 1, len_ppl):
                    recurse(npi, sks, ppl)
            
            sks.update(temp)
            ppl.pop()
        
        for i in range(len_ppl):
            recurse(i, set(req_skills), [])
        
        return self.res


sol = Solution()
p = [["java","nodejs","reactjs"], [["java"],["nodejs"],["nodejs","reactjs"]]]
# p = [["algorithms","math","java","reactjs","csharp","aws"], [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]]
print(sol.smallestSufficientTeam(*p))
