class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        
        d={}
        for i,x in enumerate(T):
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        
        r=""
        
        for x in S:
            if x in d:
                r=r+x*d[x]
                del d[x]
            
        for x in d:
            r=r+x*d[x]
            
        return (r)
