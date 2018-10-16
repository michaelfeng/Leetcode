from Queue import Queue
class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.queue = Queue()
        self.size = size
        self.sum = 0.0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        self.sum += val
        if self.queue.size() == self.size:
            self.sum -= self.queue.get()
        self.queue.put(val)
        return self.sum*1.0 / self.queue.size()

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)
