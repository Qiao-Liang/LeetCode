from collections import defaultdict

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        user_map = {}
        dis_set = {}
        temp = defaultdict(list)
        rank = defaultdict(int)
                
        def find(x):
            if x != dis_set[x]:
                dis_set[x] = find(dis_set[x])
                
            return dis_set[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            
            if rank[px] > rank[py]:
                dis_set[py] = dis_set[px]
                rank[px] += 1
            else:
                dis_set[px] = dis_set[py]
                rank[py] += 1
        
        for acc in accounts:
            for a in acc[1:]:
                user_map[a] = acc[0]
                
                if a not in dis_set:
                    dis_set[a] = a

                union(acc[1], a)
        
        for key in dis_set.keys():
            temp[find(key)].append(key)
            
        return [[user_map[key]] + sorted(val) for key, val in temp.items()]


sol = Solution()
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
# accounts = [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]
print(sol.accountsMerge(accounts))
# [["Alex","Alex0@m.co","Alex4@m.co","Alex5@m.co"],["Ethan","Ethan0@m.co","Ethan3@m.co"],["Gabe","Gabe0@m.co","Gabe2@m.co","Gabe3@m.co","Gabe4@m.co"],["Kevin","Kevin2@m.co","Kevin4@m.co"]]
# [['Alex', 'Alex0@m.co', 'Alex4@m.co', 'Alex5@m.co'], ['Ethan', 'Ethan0@m.co', 'Ethan3@m.co'], ['Kevin', 'Kevin2@m.co', 'Kevin4@m.co'], ['Gabe', 'Gabe0@m.co'], ['Gabe', 'Gabe2@m.co', 'Gabe3@m.co', 'Gabe4@m.co']]
