"""
173. Binary Search Tree Iterator
"""
class BSTIterator:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.allleft=[]
        self.pushallleft(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        x=self.allleft.pop()
        self.pushallleft(x.right)
        return x.val
        
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.allleft!=[]
        
        
    def pushallleft(self,root):
        
        while root:
            self.allleft.append(root)
            root=root.left
