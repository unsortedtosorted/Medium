class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l=[]
        

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.l.append(timestamp)
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        
        if timestamp<=300:
            return len(self.l)
        
        if timestamp>300:
            diff=timestamp-300
            y=False
            
            for i,x in enumerate(self.l):
                if x>diff:
                    y=True
                    break
            
            if y:
                self.l=self.l[i:]
                return len(self.l)
            else:
                return 0
            


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
