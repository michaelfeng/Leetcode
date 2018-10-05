class TwoSum:
    def __init__(self):
        self.d = {}
    
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        if number not in self.d:
            self.d[number] = 1
        else:
            self.d[number] = self.d[number] + 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for k, v in self.d.items():
            left = value - k
            if left == k and self.d[k] > 1 or left != k and left in self.d:
                return True
            continue
        return False
