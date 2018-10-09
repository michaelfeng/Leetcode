class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if n == 0:
            return False
        if len(edges) != n-1:
            return False
            
        neighbors = {i:[] for i in xrange(n)}
        for edge in edges:
            pre, next = edge[0], edge[1]
            neighbors[pre].append(next)
            neighbors[next].append(pre)
        
        # print neighbors
        
        queue = collections.deque([0])
        visit = set([])    
        while queue:
            for _ in xrange(len(queue)):
                node = queue.popleft()
                visit.add(node)
                for neighbor in neighbors[node]:
                    if neighbor not in visit:
                        queue.append(neighbor)
        # print visit
        return len(visit) == n
                    
            
            
        
