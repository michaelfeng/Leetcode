import Queue
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = Queue.Queue()
        self.q2 = Queue.Queue()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q1.put(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        item = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1
        return item
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        item = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1
        self.q1.put(item)
        return item
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q1.qsize() == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
