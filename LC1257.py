class Solution:
    def findSmallestRegion(self, regions, region1: str, region2: str) -> str:
        dic = {r[0]: set(r[1:]) for r in regions}
        
        if region2 in dic and region1 in dic[region2]:
            return region2
        
        if region1 in dic and region2 in dic[region1]:
            return region1

        self.paths = []
        
        def dfs(rgs, rg, p):
            if rgs in dic:
                if rg in dic[rgs]:
                    p.append(rgs)
                    p.append(rg)
                    self.paths.append(p[:])
                else:
                    p.append(rgs)

                    for r in dic[rgs]:
                        dfs(r, rg, p)

                    p.pop()

        dfs(regions[0][0], region1, [])
        dfs(regions[0][0], region2, [])

        s = set(self.paths[0])

        for r in reversed(self.paths[1]):
            if r in s:
                return r

sol = Solution()
# p = [[["Earth","North America","South America"],
# ["North America","United States","Canada"],
# ["United States","New York","Boston"],
# ["Canada","Ontario","Quebec"],
# ["South America","Brazil"]],
# "Canada",
# "Quebec"]
p = [[["zDkA","GfAj","lt"],["GfAj","rtupD","og","l"],["rtupD","IT","jGcew","ZwFqF"],["og","yVobt","EjA","piUyQ"],["IT","XFlc","W","rB"],["l","GwQg","shco","Dub","KwgZq"],["jGcew","KH","lbW"],["KH","BZ","sauG"],["yVobt","Aa","lJRmv"],["BZ","v","zh","oGg","WP"],["XFlc","Sn","ftXOZ"],["sauG","If","nK","HHOr","yEH","YWMgF"],["GwQg","Mfb","gr","S","nQ"],["shco","xsUkW"],["xsUkW","Cssa","TgPi","qx"],["v","SAH","Rjr"],["lt","Q","fWB","a","Wk","zpqU"],["If","e","y","quEA","sNyV"],["piUyQ","G","aTi"],["Sn","rVIh","twv","pYA","Ywm"],["zh","PWeEf"],["Mfb","GEs","XjpeC","p"],["GEs","oXMG","tNJYJ"],["SAH","bmFhM"],["bmFhM","SOvB","RWsEM","z"],["SOvB","iD","pLGYN","Zqk"],["Dub","PnGPY"],["a","TekG","zp"],["XjpeC","vK","aaO","D"],["pLGYN","ldb"],["oGg","x"],["nQ","IOw"],["Aa","wmYF"],["Zqk","th"],["ZwFqF","GDl"],["th","JyOSt","ALlyw"],["lbW","M"],["yEH","UY","GIwLp"],["JyOSt","i"],["x","dclJ"],["wmYF","xreBK"],["PnGPY","Ev","lI"],["ALlyw","jguyA","Mi"],["oXMG","uqe"],["sNyV","WbrP"]]
,"RWsEM","GfAj"]
print(sol.findSmallestRegion(*p))
