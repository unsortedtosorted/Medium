class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        l=[]
        a=[]
        push=0
        pop=0
        i=0
        
        
        for x in s:
            if x=="(":
                l.append(i)
            elif x=="*":
                push+=1
                pop+=1
                a.append(i)
            elif x==(")"):
                if len(l)<=0:
                    if pop>0:
                        pop-=1
                        push-=1
                        a.pop()
                    else:
                        return False
                else:
                    l.pop()
            i+=1
        
        a.sort()
        l.sort()

        while len(l)>0 and len(a)>0:
            if a[-1]>l[-1]:
                l.pop()
                a.pop()
            else:
                return False
        
        if len(l)==0:
            return True
        return False
        
