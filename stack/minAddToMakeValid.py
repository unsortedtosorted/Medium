class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        l=[]
        i=0
        for x in S:
            if x=="(":
                l.append(x)
            else:
                if len(l)>0:
                    l.pop()
                else:
                    i+=1
        
        return (i+len(l))
