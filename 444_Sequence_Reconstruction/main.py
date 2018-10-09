class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        indegree = {node: 0 for seq in seqs for node in seq}
        neighbors = {node: [] for seq in seqs for node in seq}
        
        for seq in seqs:
            for i in xrange(len(seq)-1):
                pre, next = seq[i], seq[i+1]
                indegree[next] += 1
                neighbors[pre].append(next)
            
        # print indegree, neighbors
        queue = collections.deque([])
        for node, degree in indegree.items():
            if degree == 0:
                queue.append(node)
        
        order = []
        while len(queue) == 1:
            for _ in xrange(len(queue)):
                node = queue.popleft()
                order.append(node)
                for neighbor in neighbors[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
            
        # print '#', order, len(queue)
        if len(queue) > 1: return False
        return order == org
                    
