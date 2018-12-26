class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        if dividend==0:
            return 0
        
        result=0
        temp2=0
        flag=False
        
        if divisor>0 and dividend<0:
            flag=True
        
        if divisor<0 and dividend>0:
            flag=True
            
        divisor=abs(divisor)
        dividend=abs(dividend)
        
        temp=divisor
        rem=dividend
        
        

        if dividend<divisor:
            return 0
            
            
        while dividend>=divisor:
            count=1
            temp=divisor
            
            while temp<=dividend:
                temp=temp<<1
                count=count<<1
            
            temp=temp>>1
            count=count>>1
            temp2=count+temp2
            dividend=dividend-temp
            print (count)
            print (temp2)
        
        if flag:
            return -temp2
        
        if temp2>=2147483648:
            return 2147483648-1
        
        return temp2
