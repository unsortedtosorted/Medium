class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        
        self.l=None
        self.check=False
        
        def inOrder(root):
            if root and not self.check:
                inOrder(root.left)
                if (root.val)>p.val and not self.check:
                    self.l= (root.val)
                    self.check=True
                inOrder(root.right)
                
        inOrder(root)
        return self.l
