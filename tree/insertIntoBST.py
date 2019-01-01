class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        self.inserted=False
        def insertAfterNode(root):
            
            if root and not self.inserted:
                if val<root.val:
                    
                    if not root.left:
                        root.left=TreeNode(val)
                    else:
                        insertAfterNode(root.left)
                        self.inserted=True
                elif root.val<val:
                    if not root.right:
                        root.right=TreeNode(val)
                    else:
                        insertAfterNode(root.right)
                        self.inserted=True
            else:
                return
        
        insertAfterNode(root)
        return root
        
