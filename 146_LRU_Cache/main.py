class Node:  

    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.suc = self
        self.pre = self
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.len = 0
        self.capacity = capacity
        self.hash = {}
        self.head = Node()
    
    def followNode(self, node, new):
        before, after = node, node.suc
        
        before.suc, new.pre = new,before
        new.suc, after.pre = after, new
    
    def removeNode(self, node):
        before, after = node.pre, node.suc
        
        before.suc, after.pre = after, before

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash:
            node = self.hash[key]
            self.removeNode(node)
            last = self.head.pre
            self.followNode(last,node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.hash:  # 2 !!! when use hash,always think about repeat of key, discuss seperately
            node = self.hash[key]
            node.val = value
            self.removeNode(node)
            last = self.head.pre
            self.followNode(last,node)
        else:
            self.len += 1
            node = Node(key,value)
            last = self.head.pre
            self.followNode(last,node)
            self.hash[key] = node
        
        if self.len > self.capacity:
            first = self.head.suc
            del self.hash[first.key]
            self.removeNode(first)
            self.len -= 1
