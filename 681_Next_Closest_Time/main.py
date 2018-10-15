class Solution:
    """
    @param time: the given time
    @return: the next closest time
    """
    def nextClosestTime(self, time):
        # write your code here
        h, m = time.split(":")
        curr = int(h) * 60 + int(m)  # 换算成分钟数
        result = None
        for i in range(curr+1, curr+1441):
            t = i % 1440 # mod得到当天的分钟数
            h, m = t // 60, t % 60 
            result = "%02d:%02d" % (h, m)
            if set(result) <= set(time): # 只到result里的元素个数小于等于原时间，说明没有用到额外的元素
                break
        return result
