"""

Brute Force TLE:

1. At each day check if curr day is in range of last bought ticket
2. If oppurtunity to buy, try all 3 options


"""


class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        
        self.m = sys.maxsize
        def decision(lastcost,curr,passDaysMin,passDaysMax):

            if curr == len(days):
                self.m = min(lastcost,self.m)
                return
                    
            if passDaysMin<=days[curr]<=passDaysMax:
                currcost = 0
                decision(lastcost+currcost,curr+1,passDaysMin,passDaysMax)
                return
                
         
            #buy 1 day pass
            currcost = costs[0]
            passDays = 0
            decision(lastcost+currcost,curr+1,0,0)
            
            
            #buy 7 day pass
            currcost = costs[1]
            passDays = 6
            decision(lastcost+currcost,curr+1,days[curr],days[curr]+6)
            
            #buy 30 day pass
            currcost = costs[2]
            passDays = 29
            decision(lastcost+currcost,curr+1,days[curr],days[curr]+29)
    
    
        decision(0,0,0,0)
        return self.m
        
