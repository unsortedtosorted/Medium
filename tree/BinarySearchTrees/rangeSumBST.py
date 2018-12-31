# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.l=0
        def inOrder(root):
            if root:
                if root.val>R:
                    inOrder(root.left)
                if root.val<L:
                    inOrder(root.right)
                if L<=root.val<=R:
                    self.l+=root.val
                    inOrder(root.left)
                    inOrder(root.right)
        inOrder(root)
        return (self.l)
            
