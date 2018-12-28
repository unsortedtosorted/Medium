class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        
        bucket=[None]*(len(s)+1)
        
        d={}
        
        for x in s:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        
        for x in d:
            ind=d[x]
            if bucket[ind]==None:
                bucket[ind]=[x]
            else:
                bucket[ind].append(x)
        
        r=""
        
        for x in range(len(s),-1,-1):
            if bucket[x]:
                for y in bucket[x]:
                    r=r+y*x
        
            
        return r
