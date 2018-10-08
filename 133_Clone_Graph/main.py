# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return None
        root = node
        queue = collections.deque([node])
        visit = set([node])
        
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)
        
        dict = {}
        # initial all node with value
        for node in visit:
            dict[node] = UndirectedGraphNode(node.label)
        
        # copy neighbors
        for node in visit:
            new_node = dict[node]
            for neighbor in node.neighbors:
                new_neighbor = dict[neighbor]
                new_node.neighbors.append(new_neighbor)
        
        return dict[root]
        
        
        
