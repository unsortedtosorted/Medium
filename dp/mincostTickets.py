"""
983. Minimum Cost For Tickets

1. dp algo is chose the minimum from:
    - buy one day pass + dp[i+1]
    - buy 7 day pass + dp [i+7]
    - buy 30 day pass + dp[i+30]
    
    return min



"""


class Solution(object):
    def mincostTickets(self, days, cost):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        
        self.days = set()
        
        for x in days :
            
            self.days.add(x)
            
            
        
        self.memo = {}
       
        def dp(i):
            
            if i > 365:
                return 0
            
            if i in self.memo:
                return self.memo[i]
            
            
            
            if i in self.days:
                
                ans = min(dp(i+1)+cost[0],dp(i+7)+cost[1],dp(i+30)+cost[2])
            
            else:
                ans = dp(i+1)
            
            
            self.memo[i] = ans
            
            return self.memo[i]
            
        
        return dp(1)

            
