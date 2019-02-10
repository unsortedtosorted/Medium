"""
990. Satisfiability of Equality Equations

1. first go through all equation with ==
2. go through all != equations:
    find x and y
      if x==y:
      return False

"""

class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        
        
        self.equals = [None]*26
        
        for x in range(0,26):
            self.equals[x] = x

        
        def find(a):
            if self.equals[a]!=a:
                self.equals[a] = find(self.equals[a])
                
            return self.equals[a]
                
            
        def union(a,b):
            
            i,j=find(a),find(b)
            if i!=j:
                self.equals[i] = j
                
            
        for x in equations:
            if '!' not in x:
                a = ord(x[0])-ord('a')
                b = ord(x[-1])-ord('a')
                union(a,b)
        
        for x in equations:
            
            if '!' in x:
                
                a = find(ord(x[0])-ord('a'))
                b = find(ord(x[-1])-ord('a'))
                
                if a==b:
                    return False
        return True
            
