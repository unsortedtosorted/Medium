import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
    
        d={}
        
        #Run Time O(n)
        for x in nums:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
         
        h=[]
        
        #Run Time O(k)
        for x in d.keys():
            heapq.heappush(h, (d[x], x))
        
        
        r=[None]*k
        
        for i,x in enumerate(heapq.nlargest(k,h)):
            r[i]=x[1]
            i+=1
        return r
