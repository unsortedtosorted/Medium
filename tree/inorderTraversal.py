class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        r=[]
        
        def inOrder(root):
            if root:
                inOrder(root.left)
                r.append(root.val)
                inOrder(root.right)
            else:
                return
        
        inOrder(root)
        return (r)
