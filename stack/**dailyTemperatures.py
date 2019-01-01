from collections import *
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        return (self.usingStack(T))
    
    def usingStack(self,T):
        l=deque()
        l.append((T[-1],len(T)-1))
        
        i=len(T)-2
        r=[0]*(len(T))
        r[i+1]=0
        
        while i>-1:
            if T[i]>=l[0][0]:
                while len(l)>0 and l[0][0]<=T[i]:
                    l.popleft()
                if len(l)>0:
                    r[i]=(l[0][1]-i)
                else:
                    r[i]=0
            elif T[i]<l[0][0]:
                r[i]=(l[0][1]-i)
                
            l.appendleft((T[i],i))
            i-=1
            
        return (r)
        
        
    def Tle2(self,T):
        
            d={}
            for i,v in enumerate(T):
                if v in d:
                    d[v].append(i)
                else:
                    d[v]=deque()
                    d[v].append(i)
        
            r=[]
            for i,v in enumerate(T):
                temp=v+1
                m=float('inf')
                while temp<101:
                    if temp in d:
                        while len(d[temp])>0:
                            if d[temp][0]>i:
                                if d[temp][0]<m:
                                    m=d[temp][0]
                                break
                            
                            else:
                                d[temp].popleft()
                
                    temp+=1
                if m==float('inf'):
                    r.append(0)
                else:
                    r.append(m-i)
            return (r)
        
   
    def bruteforce(self,T):
        if len(T)<=1:
            return [0]
        
        curr=0
        nextWarm=1
        r=[]
        
        while curr<len(T):
            if nextWarm>=len(T):
                r.append(0)
                curr+=1
                nextWarm=curr+1
                continue
            if T[nextWarm]>T[curr]:
                r.append(nextWarm-curr)
                curr+=1
                nextWarm=curr+1
            elif T[nextWarm]<=T[curr]:
                nextWarm+=1
        
        return (r)
