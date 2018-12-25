class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Remove leading spaces
        if len(s)<1:
            return ""
        i=0
        for x in s:
            if x==" ":
                i+=1
            else:
                break
        if i==len(s):
            return ""
        
        s=s[i:]
        
        #Remove trailling spaces
        i=len(s)-1
        j=0
        
        while i>-1:
            if s[i]==" ":
                j+=1
                i-=1
            else:
                break
        s=s[:len(s)-j]
        
        temp=""
        r=""
        
        for x in s:
            if x!=" ":
                temp=temp+x
            else:
                if temp!="":
                    r=temp+" "+r
                    temp=""
        
        r=temp+" "+r
        if len(r)>1:
            r=r[0:len(r)-1]
        return r
            
