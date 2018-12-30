lass Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans=[]
        
        seen=set()
        def valid(A):
            bal=0
            for x in A:
                if bal<0:
                    return False
                if x=="(":
                    bal+=1
                else:
                    bal-=1
            return bal==0
            
        
        def generate(A):
            if len(A)==2*n:
                if  A not in seen and valid(A):
                    ans.append(A)
                    seen.add(A)
            else:
                generate(A+"(")
                generate(A+")")

        generate("")
        return ans
