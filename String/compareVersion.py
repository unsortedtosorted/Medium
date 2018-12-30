class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        v1=version1.split(".")
        v2=version2.split(".")
        
        for i in range(max(len(v1),len(v2))):
            v1n=0
            v2n=0
            if i<len(v1):
                v1n=int(v1[i])
            if i<len(v2):
                v2n=int(v2[i])
            
            if v1n==v2n:
                continue
            elif v1n>v2n:
                return 1
            else:
                return -1
        
        return 0
