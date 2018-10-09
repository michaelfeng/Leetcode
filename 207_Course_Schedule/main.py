class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # node: indgreee num
        node_in_degree = self.get_in_degree(numCourses, prerequisites)
        # node: adjcent node list
        node_adj = self.get_adj_node(numCourses, prerequisites)
        # print node_adj
        queue = collections.deque([])
        order = []

        for node, indegree in node_in_degree.items():
            if indegree == 0:
                queue.append(node)
                
        # print queue
        level = 0
        while queue:
            level += 1
            node = queue.popleft()
            order.append(node)
            for neighbor in node_adj[node]:
                node_in_degree[neighbor] -= 1
                if node_in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # print len(order), order, numCourses, level
        if len(order) == numCourses:
            return True
        return False
        
        
    def get_in_degree(self, numCourses, prerequisites):
        node_in_degree = {i: 0 for i in range(numCourses)}
        for requisite in prerequisites:
            node_in_degree[requisite[0]] += 1
        return node_in_degree
    
    def get_adj_node(self, numCourses, prerequisites):
        node_adj = {i: [] for i in range(numCourses)}
        for requisite in prerequisites:
            node_adj[requisite[1]].append(requisite[0])
        return node_adj
        
