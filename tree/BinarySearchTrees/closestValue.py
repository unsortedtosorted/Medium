class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        
        
        self.diff=sys.maxsize-1
        self.val=None
        
        def inOrder(root):
            
            if root:
                
                x=abs(float(root.val)-target)
                if x<self.diff:
                    self.diff=x
                    self.val=root.val
                if root.val>target:
                    inOrder(root.left)
                elif root.val<target:
                    inOrder(root.right)
                
        inOrder(root)            
        return self.val
