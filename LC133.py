# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        
        self.visited = {}

        def dfs(node):
            if node.label in self.visited:
                return self.visited[node.label]

            new_node = UndirectedGraphNode(node.label)
            self.visited[new_node.label] = new_node

            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))

            return new_node

        return dfs(node)


    def cloneGraph2(self, node):
        if not node:
            return None

        visited = set([])
        created_nodes = {}
        queue = [node]

        while queue:
            temp = queue.pop(0)

            if temp not in visited:
                created_nodes[temp] = UndirectedGraphNode(temp.label)
                queue.extend(temp.neighbors) 
                visited.add(temp)
            
        visited = set([])
        queue = [node]

        while queue:
            temp = queue.pop(0)

            if temp not in visited:
                created_nodes[temp].neighbors = [created_nodes[neighbor] for neighbor in temp.neighbors]
                queue.extend(temp.neighbors)
                visited.add(temp)

        return created_nodes[node]


node0 = UndirectedGraphNode(0)
node1 = UndirectedGraphNode(1)
node2 = UndirectedGraphNode(2)

node0.neighbors = [node1, node2]
node1.neighbors = [node2]
node2.neighbors = [node2]

sol = Solution()
head = sol.cloneGraph(node0)
print head
        