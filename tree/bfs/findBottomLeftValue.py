from collections import *
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
    
        q=deque()
        q.appendleft((root,0))
        maxLevel=-sys.maxsize-1
        
        while len(q)>0:
            temp=q.pop()
            if temp[0]:   
                node=temp[0]
                level=temp[1]
                if level>maxLevel:
                    maxLevel=level
                    val=node.val
                q.appendleft((node.left,level+1))
                q.appendleft((node.right,level+1))
        
        return (val)
