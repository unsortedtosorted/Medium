class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        temp=0
        
        def checkrow(row):
            i=0
            for l in picture[row]:
                if l=='B':
                    i+=1
            
            return i==1
        
        
        def checkcol(col):
            flag=0
            for row,x in enumerate(picture):
                if (x[col])=='B':
                    flag+=1
            
            return flag==1
            
       
        
        for i,x in enumerate(picture):
            for j,y in enumerate(x):
                if y=='B':
                    if checkrow(i) and checkcol(j):
                        temp+=1
        
        return (temp)
