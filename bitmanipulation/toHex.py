class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        if num<0:
            num += 2 ** 32
        print (2**32)
        print (num+2**32)
        print (-num+2**32)
        
        
        r=[]
        while num>=16:
            rem=num%16
            num//=16
            
            if rem==10:
                r.append('a')
            elif rem==11:
                r.append('b')
            elif rem==12:
                r.append('c')
            elif rem==13:
                r.append('d')
            elif rem==14:
                r.append('e')
            elif rem==15:
                r.append('f')
            else:
                r.append(str(rem))
        
        if num==10:
            r.append('a')
        elif num==11:
            r.append('b')
        elif num==12:
            r.append('c')
        elif num==13:
            r.append('d')
        elif num==14:
            r.append('e')
        elif num==15:
            r.append('f')
        else:
            r.append(str(num))
        
       
        return ("".join(r[::-1]))
            
