class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        
        curr=0
        last=len(piles)-1
        
        a=0
        l=0
        i=1
       
        while curr<last:    
            
            f=piles[curr]
            l=piles[last]
            
            if i%2!=0:
                if f>=l:
                    a+=f
                    curr+=1
                else:
                    a+=l
                    last-=1
            else:
                if f>=1:
                    l+=1
                    curr+=1
                else:
                    l+=1
                    last-=1
            i+=1
        
        return a>l
