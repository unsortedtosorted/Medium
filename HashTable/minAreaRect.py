"""
939. Minimum Area Rectangle

1. for a point r1,c1 and r2,c2 check if point r1,c2 and r2,c1 exist
2. if it does, find the area
3. if area less than prev value, update the area value to be returned.

Runtime: O(N^2)
space : O(N)

"""


from collections import Counter

class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        p = Counter()
        
        for x in points:
            
            r = x[0]
            c = x[1]
            
            p[r,c]+=1
        
        
        def k(p):
            return p[1],p[0]
        
        
        points = sorted(points,key = k)
        
        def getarea(r1,r2,c1,c2):
            return abs(r1-r2)*abs(c1-c2)
        
        ar = sys.maxsize
        
        for i,col1 in enumerate(points):
            for j,col2 in enumerate(points):
                if i==j:
                    continue
                    
                r1 = col1[0]
                c1 = col1[1]
                
                r2 = col2[0]
                c2 = col2[1]
                
                if r1 == r2 or c1 == c2:
                    continue
                
                if p[r1,c2]==1 and p[r2,c1]==1:
                    d = getarea(r1,r2,c1,c2)
                    
                    if d < ar:
                        ar=d
        
        if ar == sys.maxsize:
            return 0
        return ar
