class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        seen=set()
        def checkIsland(x,y,seen):
            ones=0
            #check top
            if x-1>-1 and (x-1,y) not in seen:
                if grid[x-1][y]==1:
                    seen.add((x-1,y))
                    ones+=1
                    ones+=checkIsland(x-1,y,seen)
            #check bottom
            if x+1<len(grid) and (x+1,y) not in seen:
                if grid[x+1][y]==1:
                    seen.add((x+1,y))
                    ones+=1
                    ones+=checkIsland(x+1,y,seen)
            #check left
            if y-1>-1 and (x,y-1)not in seen:
                if grid[x][y-1]==1:
                    seen.add((x,y-1))
                    ones+=1
                    ones+=checkIsland(x,y-1,seen)
            #check right
            if y+1<len(grid[x]) and (x,y+1) not in seen:
                if grid[x][y+1]==1:
                    ones+=1
                    seen.add((x,y+1))
                    ones+=checkIsland(x,y+1,seen)
            
            return ones
                    
        m=0
        for i,x in enumerate(grid):
            for j,y in enumerate(x):
                if y==1 and (i,j) not in seen:
                    seen.add((i,j))
                    ones=checkIsland(i,j,seen)+1
                    if ones>m:
                        m=ones
                    
        
        return m
