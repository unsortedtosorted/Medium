class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        n1=0
        i=0
        for x in num1[::-1]:
            n1=n1+(ord(x)-ord('0'))*(10**i)
            i+=1
        
        r=0
        i=0
        for y in num2[::-1]:
            r=r+n1*((ord(y)-ord('0'))*10**i)
            i+=1
        return str(r)
