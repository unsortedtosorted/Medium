"""

1. Keep track of co-ordinates of all black pixels seen
2. keep number of black pixels in each row
3. keep track of all bacl pixels in each col
4. iterate all black co-ordinates again and check if its row and coloumn has more than 
one blac pixel or not.

"""

class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        
        
        blackPos=[]
        
        row=[0]*len(picture)
        col=[0]*len(picture[-1])
        
        for i,x in enumerate(picture):
            for j,y in enumerate(x):
                if y=='B':
                    row[i]+=1
                    col[j]+=1
                    blackPos.append((i,j))
        

        temp=0
        
        for x in (blackPos):
            if row[x[0]]==1 and col[x[1]]==1:
                temp+=1
        
        return temp
        
