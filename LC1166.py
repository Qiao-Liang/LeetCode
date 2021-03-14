class FileSystem:

    def __init__(self):
        self.dict = {"": -1}
        
    def create(self, path: str, value: int) -> bool:
        if path[:path.rfind('/')] in self.dict:
            self.dict[path] = value
            return True
        else:
            return False
        
    def get(self, path: str) -> int:
        return self.dict[path] if path in self.dict else -1


class Node:
    def __init__(self, val):
        self.value = val
        self.children = {}


class FileSystem2:
    def __init__(self):
        self.root = Node(-1)

    def create(self, path, value):
        curr = self.root
        path = path.split('/')
        bound = len(path) - 1

        for i, name in enumerate(path[1:]):
            if name in curr.children:
                curr = curr.children[name]
            else:
                if i == bound:
                    curr.children[name] = Node(value)
                    return True
                else:
                    return False
    
    def get(self, path):
        curr = self.root

        for name in path.split('/')[1:]:
            if name in curr.children:
                curr = curr.children[name]
            else:
                return -1

        return curr.value


# class Folder(object):
#     def __init__(self, name, prnt):
#         self.name = name
#         self.children = {}
#         self.content = None
    
#         if prnt:
#             prnt.children[name] = self
        
#     def find(self, root, path):
#         children = {root.name: root}
#         res = None
#         depth = 0

#         for name in path:
#             if name in children:
#                 depth += 1
#                 res = children[name]
#                 children = res.children
        
#         return res, depth


# class FileSystem(object):

#     def __init__(self):
#         self.root = Folder("", None)
        
#     def create(self, path, value):
#         """
#         :type path: str
#         :type value: int
#         :rtype: bool
#         """
#         path = path.split('/')
#         prnt, depth = self.root.find(self.root, path)

#         if prnt and len(path) - depth == 1:
#             content = path[path.index(prnt.name) + 1:]

#             for name in content:
#                 temp = Folder(name, prnt)
#                 prnt = temp

#             prnt.content = value
#             return True
#         else:
#             return False

#     def get(self, path):
#         """
#         :type path: str
#         :rtype: int
#         """
#         path = path.split('/')
#         prnt, depth = self.root.find(self.root, path)

#         return prnt.content if prnt and depth == len(path) else -1


# Your FileSystem object will be instantiated and called as such:
fileSystem = FileSystem2()
fileSystem.create("/leet", 1)
fileSystem.create("/leet/code", 2)
fileSystem.get("/leet/code")
print(fileSystem.create("/c/d", 1))
print(fileSystem.get("/c"))
