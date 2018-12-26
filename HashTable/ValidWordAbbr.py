class ValidWordAbbr:

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.d={}
        
        for x in dictionary:
            s=self.getAbbri(x)
            if s in self.d.keys():
                self.d[s].add(x)
            else:
                s1=set()
                s1.add(x)
                self.d[s]=s1
                    
        
                    
                
            
    def getAbbri(self,x):
        
        if len(x)<=2:
            return x
        start=x[0]
        stop=x[-1]
        num=len(x)-2
        s=start+str(num)+stop
        return s
        

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        s=self.getAbbri(word)
        
        if s not in self.d.keys():
            return True
        else:
            l=self.d[s]
            
            if len(l)==1:
                if word in l:
                    return True
                else:
                    return False
            else:
                return False
            
            
        
        
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
