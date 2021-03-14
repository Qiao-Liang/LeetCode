from collections import defaultdict

class Solution:
    def generateSentences(self, synonyms, text: str):
        lt = text.split(' ')
        bound = len(lt) - 1
        self.res = []
        groups = {}
        dic = defaultdict(set)

        for s in synonyms:
            for w in s:
                groups[w] = w
        
        def find(i):
            if i != groups[i]:
                groups[i] = find(groups[i])

            return groups[i]

        def union(x, y):
            tx, ty = find(x), find(y)

            if tx != ty:
                groups[tx] = groups[ty]

        for x, y in synonyms:
            union(x, y)

        for k in groups:
            find(k)

        for k, v in groups.items():
            dic[v].add(k)

        sets = list(dic.values())
        
        def recurse(lt, i):
            if i > bound:
                self.res.append(' '.join(lt))
            else:
                for s in sets:
                    if lt[i] in s:
                        ow = lt[i]
                    
                        for w in s:
                            lt[i] = w
                            recurse(lt, i + 1)
                        
                        lt[i] = ow
                else:
                    recurse(lt, i + 1)
            
        recurse(lt, 0)
        self.res = list(set(self.res))
        self.res.sort()
        return self.res


sol = Solution()
p = [[["happy","joy"],["sad","sorrow"],["joy","cheerful"]], "I am happy today but was sad yesterday"]
print(sol.generateSentences(*p))
