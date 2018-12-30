class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        B=[]
        
        for i,x in enumerate(A):
            B.append((i,x))
        
        
        def fun(x):
            return x[1],
        B=sorted(B,key=fun)
        
        ans=0
        m=sys.maxsize-1
        
        
        for x in range(0,len(B)):
           
            ans=max(ans,B[x][0]-m)
            m=min(m,B[x][0])
            
        
        return(ans)
            
