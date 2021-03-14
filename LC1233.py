class Solution:
    def removeSubfolders(self, folder):
        folder.sort()
        folder_set = set([])
        
        for fd in folder:
            temp = fd.split('/')
            
            for i in range(1, len(temp)):
                t = '/'.join(temp[:i])
                
                if t in folder_set:
                    break
            else:
                folder_set.add(fd)
        
        return list(folder_set)


sol = Solution()
# folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
# folder = ["/a","/a/b/c","/a/b/d"]
folder = ["/a/b/c","/a/b/ca","/a/b/d"]
print(sol.removeSubfolders(folder))
