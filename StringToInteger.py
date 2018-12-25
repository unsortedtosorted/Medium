class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        neg=None
        i=0
        temp=0
        
        
        k=0
        for i in str:
            if i==" ":
                k+=1
            else:
                break
        
        if k==len(str):
            return 0
        else:
            str=str[k:]
        
            
        i=0
        for x in str[::-1]:
            if x==" ":
                temp=0
                i=0
                continue
            elif ord("0")<=ord(x)<=ord("9") :
                if neg==None:
                    temp=temp+(ord(x)-ord("0"))*(10**i)
                    i+=1
                else:
                    i=0
                    temp=0
                    temp=temp+(ord(x)-ord("0"))*(10**i)
                    i+=1
                    neg=None
                    
            elif x==".":
                temp=0
                i=0
                continue
            elif x=="-":
                if neg==None:
                    neg=True
                else:
                    if temp>0:
                        return 0
            elif x=="+":
                if neg==None:
                    neg=False
                else:
                    if temp>0:
                        return 0
            elif not ord("0")<=ord(x)<=ord("9") and temp>=0:
                temp=0
                i=0
        
        

        if neg:
            temp=temp*-1
        if temp<=(-2**31):
            return -2**31
        if temp>=(2**31):
            return 2**31-1
            
        return (temp)
