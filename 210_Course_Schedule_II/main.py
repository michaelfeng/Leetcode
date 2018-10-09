class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        node_indegree = self.get_node_indegree(numCourses, prerequisites)
        node_edge_to = self.get_node_edge_to(numCourses, prerequisites)
        
        queue = collections.deque([])
        order = []
        
        for node, indegree in node_indegree.items():
            if indegree == 0:
                queue.append(node)
                
        while queue:
            node = queue.popleft()
            order.append(node)
            for node in node_edge_to[node]:
                node_indegree[node] -= 1
                if node_indegree[node] == 0:
                    queue.append(node)
        
        # print order
        if len(order) == numCourses:
            return order
        return []
        
    
    def get_node_indegree(self, numCourses, prerequisites):
        node_indegree = {i:0 for i in xrange(numCourses)}
        for prerequisite in prerequisites:
            node_indegree[prerequisite[0]] += 1
        return node_indegree  
   
    def get_node_edge_to(self, numCourses, prerequisites):
        node_edge_to = {i:[] for i in xrange(numCourses)}
        for prerequisite in prerequisites:
            node_edge_to[prerequisite[1]].append(prerequisite[0])
        return node_edge_to  
        
        
