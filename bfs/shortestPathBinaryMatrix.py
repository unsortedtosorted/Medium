"""
1091. Shortest Path in Binary Matrix

"""

from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        
        if grid[0][0] !=0:
            return -1
        
        if grid[len(grid)-1][len(grid)-1] !=0:
            return -1
        parent = {}
        
        q = deque()
        q.appendleft((0,0))
        
        visited = set()
        
        while len(q) > 0:
            
            curr = q.pop()
            
            
            visited.add(curr)
            r = curr[0]
            c = curr[1]
            
            
            
            if r == len(grid)-1 and c == len(grid)-1:
                break
                
            #add top
            if r-1 >=0:
                if (r-1,c) not in parent and grid[r-1][c]!=1:
                    parent[(r-1,c)] = (r,c)
                    q.appendleft((r-1,c))
                
            #add down
            if r+1 < len(grid):
                if (r+1,c) not in parent and grid[r+1][c] != 1:
                    parent[(r+1,c)] = (r,c)
                    q.appendleft((r+1,c))
                
            #add left
            if c-1 >= 0:
                if (r,c-1) not in parent and grid[r][c-1] != 1:
                    parent[(r,c-1)] = (r,c)
                    q.appendleft((r,c-1))
                
            #add right
            if c+1 < len(grid[r]):
                if (r,c+1) not in parent and grid[r][c+1] != 1:
                    parent[(r,c+1)] = (r,c)
                    q.appendleft((r,c+1))
                    
            #add top left
            if (r-1 >=0 and c-1>=0):
                if (r-1,c-1) not in parent and grid[r-1][c-1] !=1:
                    parent[(r-1,c-1)] = (r,c)
                    q.appendleft((r-1,c-1))
                
            #add top right
            
            if (r-1 >=0 and c+1< len(grid)):
                if (r-1,c+1) not in parent and grid[r-1][c+1] !=1:
                    parent[(r-1,c+1)] = (r,c)
                    q.appendleft((r-1,c+1))
                    
                
            #add bottom left
           
            if ( r+1 < len(grid) and c-1 >= 0):
                if (r+1,c-1) not in parent and grid[r+1][c-1] !=1:
                    parent[(r+1,c-1)] = (r,c)
                    q.appendleft((r+1,c-1))
                
            #add bottom right
            
            if ( r+1 < len(grid) and c+1 < len(grid) ):
                if (r+1,c+1) not in parent:
                    if grid[r+1][c+1] !=1:
                        parent[(r+1,c+1)] = (r,c)
                        q.appendleft((r+1,c+1))
                    if r+1 == len(grid)-1 and c+1 == len(grid)-1:
                        parent[(r+1,c+1)] = (r,c)
                        q.appendleft((r+1,c+1))
                        
        
        count = 1
        curr = (len(grid)-1, len(grid)-1)
        if curr not in parent:
            return -1
    
        
        while curr!= (0,0):
            count+=1
            curr = parent[curr]
        
        return count
