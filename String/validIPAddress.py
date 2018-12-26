class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        
        
        def check4(ip):
            l=ip.split(".")
            if len(l)==4:
                for x in l:  
                    try:
                        if 0<=int(x)<=255:
                            if str(int(x))!=x:
                                return "Neither"
                        else:
                            return "Neither" 
                    except ValueError:
                        return "Neither" 
            else:
                return "Neither" 
            return "IPv4"
        
     
        def check6(ip):
            l=ip.split(":")
            if len(l)==8:
                for x in l:
                    try:
                        temp=x.upper()
                        if len(temp)>4:
                            return "Neither"
                        if len(temp)==0:
                            return "Neither"
                            
                        for t1 in temp:
                            
                            if ord('0')<=ord(t1)<=ord('9') or ord('A')<=ord(t1)<=ord('F'):
                                continue
                            else:
                                return "Neither" 
                                
                                
                        
                    except ValueError:
                        
                        return "Neither" 
            else:
                return "Neither" 
            return "IPv6"
            
        if "." in IP:
            return check4(IP)
        elif ":" in IP:
            return check6(IP)
        
        else:
            return "Neither" 
