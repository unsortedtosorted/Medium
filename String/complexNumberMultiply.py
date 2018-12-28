class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        ar,ai=a.split("+")
        br,bi=b.split("+")
        
        ar=int(ar)
        br=int(br)
        bi=int(bi[:-1])
        ai=int(ai[:-1])
        
        t1=ar*br
        t2=ar*bi
        t3=ai*br
        t4=ai*bi*(-1)
        
        tr=t1+t4
        ti=t2+t3
        
        return (str(tr)+"+"+str(ti)+"i")
