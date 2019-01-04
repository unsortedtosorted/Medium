class Solution:
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        
        o = [0] * length
        
        for x in updates:
            
            start= x[0]
            stop = x[1]
            inc  = x[2]
            o[start]+=inc
            if stop+1<length:
                o[stop+1]=o[stop+1]-inc
            
        temp=o[0]
        i=1
        
        while i<length:
            o[i]+=temp
            temp=o[i]
            i+=1
        return (o)
